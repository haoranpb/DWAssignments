import requests
import time
import threading
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import random
import redis
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


ua = UserAgent()
db = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)
cookies = []
Cookie_Number = 6
Thread_Number = 25

ip_dict = {}

with open('./cookie.txt') as f: # set up cookies
    for line in f:
        cookie = {}
        line = line.strip('\n')
        for item in line.split(';'):
            item = item.strip()
            l = item.split('=')
            cookie[l[0]] = l[1]
        cookies.append(cookie)

def get_proxy():
    ip_str = requests.get("http://127.0.0.1:5010/get_all/").text
    ips = ip_str.strip()
    ips = ips[1:-1].strip()
    raw_ip_list = ips.split('\n')
    tmp = []
    for ip in raw_ip_list:
        t = ip.strip()
        t = t.strip(',')
        tmp.append(t.strip('"'))
    return random.choice(tmp)

def delete_proxy(p):
    requests.get('http://127.0.0.1:5010/delete?proxy=' + p)

def Parser(html, id, n, p):
    soup = BeautifulSoup(html, 'lxml')
    element = soup.find(id='productTitle')
    title = ''
    if element == None:
        element = soup.find('h1' ,attrs={'class': 'avu-full-width'})
        if element == None: # Error
            db.sadd('movieID', id)
            print('Robot Detect!!!!!!!!!!!!!!!!!!!!!!')
            if p in ip_dict:
                ip_dict[p] += 1
                if ip_dict[p] > 10:
                    delete_proxy(p)
            else:
                ip_dict[p] = 1
            return False
        else: # Prime Video Page
            title = element.text
    else: # Simple Page
        title = element.text
    if 'Director' not in html: # A movie must have a director
        return False
    if 'Season' not in title and 'Season' in html: # TV show
        return False
    if 'Fitness' not in title and 'Fitness' in html: # Not a moive
        return False
    if 'Music Videos' in html:
        return False
    if 'Concerts' in html:
        return False
    db.sadd('movieName', title.strip())
    return True


def GetAndParse(n):
    header = {
        'User-Agent': ua.random,
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br'
    }
    movieID = db.spop('movieID')
    url = 'https://www.amazon.com/dp/' + movieID
    p = ''
    try:
        if n%26 == 0:
            proxier = { 'https' : 'http://127.0.0.1:1087' }
            response = requests.get(url, headers=header, proxies=proxier , cookies=cookies[n%Cookie_Number], timeout=5, verify=False)
        else:
            p = get_proxy()
            proxier = { 'https' : 'http://' + p }
            response = requests.get(url, headers=header, proxies=proxier , cookies=cookies[n%Cookie_Number], timeout=10, verify=False)       
    except:
        db.sadd('movieID', movieID)
        print('Cookie Number: ' + str(n%Cookie_Number))
        print('Requests Failure!\n\n')
    else:
        if response.status_code == 404:
            print('Getting ' + url)
            print('Number ' + str(n))
            print('Page 404' + '\n\n')
        elif response.status_code == 200: # get tittle
            if Parser(response.text, movieID, n, p):
                print('Getting ' + url)
                print('Number ' + str(n))
                print('Yes!' + '\n\n')
            else:
                print('Getting ' + url)
                print('Number ' + str(n))
                print('Nope!' + '\n\n')
        else:
            print('Getting ' + url)
            print('Number ' + str(n))
            print('Something Wrong!')
            db.sadd('movieID', movieID)
            print(str(response.status_code) + '\n\n')

for i in range(100000):
    while threading.active_count()>Thread_Number: # Change
        t = 5 * random.random()
        if t < 0.5:
            t += 1.5
        elif t > 3.5:
            t -= 2.5
        time.sleep(t)
    if i%2500 == 1 and i >10:
        time.sleep(30)
    t = threading.Thread(target=GetAndParse, args=(i,))
    t.start()
    time.sleep(random.random()/3 + 0.1)


while threading.active_count()>1: # Wait the thread I created to finish
    time.sleep(0.2)
print('------------Finish-----------')

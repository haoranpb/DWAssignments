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
Thread_Number = 4
with open('./cookie.txt') as f: # set up cookies
    for line in f:
        cookie = {}
        line = line.strip('\n')
        for item in line.split(';'):
            item = item.strip()
            l = item.split('=')
            cookie[l[0]] = l[1]
        cookies.append(cookie)


def Parser(html, id, n):
    soup = BeautifulSoup(html, 'lxml')
    element = soup.find(id='productTitle')
    title = ''
    if element == None:
        element = soup.find('h1' ,attrs={'class': 'avu-full-width'})
        if element == None: # Error
            db.sadd('movieID', id)
            print('Robot Detect!!!!!!!!!!!!!!!!!!!!!!')
            print('Cookie Number: ' + str(n%Cookie_Number))
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
        'accept-encoding': 'gzip, deflate, br',
        'upgrade-insecure-requests': '1',
        'cache-control': 'max-age=0'
    }
    movieID = db.spop('movieID')
    url = 'https://www.amazon.com/dp/' + movieID
    try:
        if n%2 == 0:
            response = requests.get(url, headers=header, cookies=cookies[n%Cookie_Number],timeout=5, verify=False)
        else:
            proxier = { 'http' : 'http://127.0.0.1:1087' }
            response = requests.get(url, headers=header, proxies=proxier ,cookies=cookies[n%Cookie_Number],timeout=5, verify=False)
        
        # proxier = { 'http' : 'http://127.0.0.1:1087' }
        # response = requests.get(url, headers=header, proxies=proxier ,cookies=cookies[n%Cookie_Number],timeout=5, verify=False)

        #response = requests.get(url, headers=header, cookies=cookies[n%Cookie_Number],timeout=5, verify=False)        
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
            if Parser(response.text, movieID, n):
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
            print(response.status_code + '\n\n')

for i in range(1000):
    while threading.active_count()>Thread_Number: # Change
        t = 10 * random.random()
        if t <3.0:
            t += 3.0
        time.sleep(t)
    t = threading.Thread(target=GetAndParse, args=(i,))
    t.start()
    time.sleep(random.random()+0.5)


while threading.active_count()>1: # Wait the thread I created to finish
    time.sleep(0.2)
print('------------Finish-----------')

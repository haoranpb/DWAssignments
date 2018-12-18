"""
    Crawl the 25w data again to find the  上映时间，电影名称（含不同版本），导演，演员，类别, comments
"""
import time
import random
import threading
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import redis
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


ua = UserAgent()
db = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)
THREAD_NUM = 50
NUM = 20000
ip_dict = {}


def parser(html, raw_movie_id, proxy):
    """
        Check the Sent html
    """
    soup = BeautifulSoup(html, 'lxml')
    element = soup.find(id='productTitle')
    movie = {'id': raw_movie_id}
    # Get The Title
    if element is None:
        element = soup.find('h1', attrs={'class': 'avu-full-width'})
        if element is None: # Error
            db.sadd('raw_movie_id', raw_movie_id) # put back
            print('Robot Detect!!!!!!!!!!!!!!!!!!!!!!')
            if proxy in ip_dict:
                ip_dict[proxy] += 1
                if ip_dict[proxy] > 10:
                    requests.get('http://127.0.0.1:5010/delete?proxy=' + proxy) # delete proxy
            else:
                ip_dict[proxy] = 1
            return False
        else: # Prime Video Page
            try:
                movie = get_prime_page_info(soup, movie)
            except Exception:
                pass
    else: # Simple Page
        try:
            movie = get_normal_page_info(soup, movie)
        except Exception:
            pass

    if 'Director' not in html: # A movie must have a director
        return False
    if 'Fitness' in html: # Not a moive
        return False
    if 'Music Videos' in html:
        return False
    if 'Concerts' in html:
        return False
    if 'title' in movie and 'Season' in movie['title']:
        return False

    save_movie(movie, raw_movie_id)
    return True

def save_movie(movie, movie_id):
    """
        Save the moive into redis, judge if the movie is correct before store it into the database
    """
    if 'director' in movie and 'actor' in movie and 'title' in movie:
        if 'genre' not in movie:
            movie['genre'] = None
        if 'review' not in movie:
            movie['review'] = 0
        if 'date' not in movie:
            movie['date'] = None
        db.hmset('movie: ' + movie_id, movie)
    else:
        print('Movie ' + movie_id + 'do not have full information!')
        print('\n\n')


def get_and_parse(number):
    """
        Get raw_movie_id, proxy and html, Send them to the Parser
    """
    header = {
        'User-Agent': ua.random,
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
        'accept': 'text/html,application/xhtml+xml,application/xml;\
        q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br'
    }
    raw_movie_id = db.spop('raw_movie_id')
    url = 'https://www.amazon.com/dp/' + raw_movie_id
    r = requests.get('http://127.0.0.1:5010/get_all/').json()
    if not r:
        proxy = '127.0.0.1:1087'
    else:
        proxy = random.choice(r)
    try:
        proxier = {'https' : 'http://' + proxy}
        response = requests.get(url, headers=header, proxies=proxier, timeout=10, verify=False)
    except Exception:
        db.sadd('raw_movie_id', raw_movie_id)
        print('Requests Failure!\n\n')
    else:
        if response.status_code == 404:
            print('Getting ' + url)
            print('Number ' + str(number))
            print('Page 404' + '\n\n')
        elif response.status_code == 200: # get tittle
            if parser(response.text, raw_movie_id, proxy):
                print('Getting ' + url)
                print('Number ' + str(number))
                print('Yes!' + '\n\n')
            else:
                print('Getting ' + url)
                print('Number ' + str(number))
                print('Nope!' + '\n\n')
        else:
            print('Getting ' + url)
            print('Number ' + str(number))
            print('Something Wrong!')
            db.sadd('raw_movie_id', raw_movie_id)
            print(str(response.status_code) + '\n\n')

def get_normal_page_info(soup, movie):
    """
        Get All Info From Normal Pages
    """
    for child in soup.find('div', attrs={'class': 'content'}).ul.find_all('li'):
        text = child.text.strip()
        if 'Actor' in text:
            movie['actor'] = [item.strip() for item in text.split(':')[1].split(',')] # actor
        elif 'Director' in text:
            movie['director'] = [item.strip() for item in text.split(':')[1].split(',')] # director
        elif 'Release Date' in text:
            movie['date'] = text.split(':')[1].strip() # release date

    tmp = soup.find(id='acrCustomerReviewText').text
    movie['review'] = int(tmp[0: tmp.find('customer') - 1])  # review number
    movie['title'] = soup.find(id='productTitle').text.strip() # movie title
    movie['genres'] = soup.find('ul').find_all('li')[-1].span.a.text.strip() # genres

    return movie

def get_prime_page_info(soup, movie):
    """
        Get All Info From Normal Pages
    """
    movie['title'] = soup.find('h1', attrs={'class': 'avu-full-width'}).text.strip() # movie title
    tmp = soup.find(id='dp-summary-see-all-reviews').text
    movie['review'] = int(tmp[0: tmp.find('customer') - 1]) # review number
    movie['date'] = soup.find('span', attrs={'data-automation-id': 'release-year-badge'}).text

    for child in soup.find('table').find_all('tr'):
        text = child.text.strip()
        if 'Genre' in text:
            movie['genre'] = [item.strip() for item in text.split('\n')[-1].split(',')] # genre
        elif 'Director' in text:
            movie['director'] = [item.strip() for item in text.split('\n')[-1].split(',')] # director
        elif 'Actor' in text:
            movie['actor'] = [item.strip() for item in text.split('\n')[-1].split(',')] # actor
        elif 'date' or 'Date' in text:
            movie['date'] = [item.strip() for item in text.split('\n')[-1].split(',')] # date

    return movie

if __name__ == '__main__':
    for i in range(NUM):
        while threading.active_count() > THREAD_NUM: # Change
            t = 4 * random.random()
            if t < 0.5:
                t += 1.5
            elif t > 3.5:
                t -= 2.5
            time.sleep(t)
        t = threading.Thread(target=get_and_parse, args=(i,))
        t.start()


    while threading.active_count() > 1: # Wait the thread I created to finish
        time.sleep(0.2)
    print('------------Finish-----------')

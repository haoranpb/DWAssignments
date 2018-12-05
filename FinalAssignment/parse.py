"""
    The file for test
    上映时间，电影名称（含不同版本），导演，演员，类别, comments
"""
import requests
from bs4 import BeautifulSoup


def get_normal_page_info(url, movie):
    """
        Get All Info From Normal Pages
    """
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    for child in soup.find('div', attrs={'class': 'content'}).ul.find_all('li'):
        text = child.text.strip()
        if 'Actor' in text:
            movie['actor'] = [item.strip() for item in text.split(':')[1].split(',')] # actor
        elif 'Director' in text:
            movie['director'] = [item.strip() for item in text.split(':')[1].split(',')] # director
        elif 'Release Date' in text:
            movie['date'] = text.split(':')[1].strip() # release date

    tmp = soup.find(id='acrCustomerReviewText').text
    movie['review'] = tmp[0: tmp.find('customer') - 1]  # review number
    movie['title'] = soup.find(id='productTitle').text.strip() # movie title
    movie['genres'] = soup.find('ul').find_all('li')[-1].span.a.text.strip() # genres

    return movie

def get_prime_page_info(url, movie):
    """
        Get All Info From Normal Pages
    """
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    movie['title'] = soup.find('h1', attrs={'class': 'avu-full-width'}).text.strip() # movie title
    tmp = soup.find(id='dp-summary-see-all-reviews').text
    movie['review'] = tmp[0: tmp.find('customer') - 1] # review number
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

if __name__ == "__main__":
    URL = 'https://www.amazon.com/dp/0767821998'
    P_URL = 'https://www.amazon.com/dp/B0030DCAYS'
    # movie = get_normal_page_info(URL, {})
    get_prime_page_info(P_URL, {})
    # print(movie)

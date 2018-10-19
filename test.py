import requests
# from bs4 import BeautifulSoup

# cookies = []
# with open('./cookie.txt') as f:
#     for line in f:
#         cookie = {}
#         line = line.strip('\n')
#         for item in line.split(';'):
#             item = item.strip()
#             l = item.split('=')
#             cookie[l[0]] = l[1]
#         cookies.append(cookie)

# print(cookies)



proxier = { 
    'http': 'http://185.213.148.122:443'
}
r = requests.get('http://httpbin.org/ip', proxies=proxier, timeout=3)
print(r.text)

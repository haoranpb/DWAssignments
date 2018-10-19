import requests

with open('./ip.txt', 'r') as f:
    for line in f:
        proxier = { 
            'http': 'http://' + line.strip('\n'),
            'https': 'https://' + line.strip('\n')
        }
        try:
            r = requests.get('https://www.baidu.com', proxies=proxier, timeout=2)
            print(r.status_code)
        except:
            print('Fail')
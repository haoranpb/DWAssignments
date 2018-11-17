import requests
r = requests.get('http://127.0.0.1:5010/get_all/').json()
print(len(r))

import requests
import random

r = requests.get('http://127.0.0.1:8080/get_all/').json()
print(r)
print(random.choice(r))
import redis

db = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)

f = open('./movieName.txt', 'w')
# parsing movie name

# for tittle in db.sscan_iter('movieName'):
#     if 'Season' in tittle or 'Volume' in tittle or 'Vol.' in tittle:
#         continue
#     name = tittle.strip()
#     name = name.split('(')[0]
#     name = name.strip()
#     name = name.strip('VHS')
#     name = name.strip('[VHS]')
#     name = name.strip()
#     f.write(name + '\n')

while(db.scard('movieName') > 0):
    tittle = db.spop('movieName')
    if 'Season' in tittle or 'Volume' in tittle or 'Vol.' in tittle:
        continue
    name = tittle.strip()
    name = name.split('(')[0]
    name = name.strip()
    name = name.strip('VHS')
    name = name.strip('[VHS]')
    name = name.strip()
    if tittle == name:
        f.write(name + '\n')
    else:
        db.sadd('movieName', name)

f.close()
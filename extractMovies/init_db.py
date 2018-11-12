import redis

db = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)

with open('./movieID.txt', 'r') as f:
    for line in f:
        db.sadd('movieID', line.strip('\n'))
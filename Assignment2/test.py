import redis

db = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)
# print(db.keys())
i = 0
with open('../movieID.txt', 'r') as file:
    for line in file:
        i += 1
print(i)

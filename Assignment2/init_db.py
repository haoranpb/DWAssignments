"""
    Add all raw_movie_id into redis database
"""
import redis

db = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)

with open('../movieID.txt', 'r') as f:
    for line in f:
        db.sadd('raw_movie_id', line.strip('\n'))

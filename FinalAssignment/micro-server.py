"""
    Micro Server For My Redis Part
"""
import json
from flask import request, Flask
import redis

app = Flask(__name__)
db = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)

@app.route('/moviequery', methods=['GET', 'POST'])
def moviequery():
    pass

@app.route('/relationquery', methods=['GET', 'POST'])
def relationquery():
    pass
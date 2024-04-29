import os
from flask import Flask
from redis import Redis

app = Flask(__name__)

#RedisDb = Redis(host=os.getenv('HOST'), port=os.getenv('PORT'))
RedisDb = Redis(host='192.168.122.11', port=6380)

VisitorCount = 0

@app.route('/')
def hello_world():
    RedisDb.incr('VisitorCount')
    VisitorCount = str(RedisDb.get('VisitorCount'), 'utf-8')
    return "Hello World !! Visitor Count: " + VisitorCount



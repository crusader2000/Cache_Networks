from lfu import *
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

evict_lfu(r)
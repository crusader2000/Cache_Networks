import redis
import os

r = redis.Redis(host='localhost', port=6379, db=0)

data = os.listdir("../data/")

for i in range(len(data)):
    print(data[i])
    f = open('../data/'+data[i], 'rb')
    file_content = f.read()
    f.close()

    r.set(data[i],file_content)
    r.set(data[i]+':lfu_count',0)

print(r.keys())
print()
memory_stats = r.info(section="memory")
print("USED MEMORY", memory_stats["used_memory_human"])
print("MAX MEMORY", memory_stats["maxmemory_human"])
print()

import redis

servers = ["6379","6380","6381","6382","6383","6384"]

def print_keys(r):
    all_keys = [x.decode('ascii') for x in r.keys()]
    all_keys.sort()
    print(all_keys)

for port_num in servers:
    try:
        r = redis.Redis(host='localhost', port=port_num, db=0)
        print(port_num)
        print_keys(r)
        memory_stats = r.info(section="memory")
        print("USED MEMORY", memory_stats["used_memory_human"])
        print("MAX MEMORY", memory_stats["maxmemory_human"])
        print()
        r.close()
    except:
        pass
import numpy as np
import redis

master_server = "6379"

def get_data_from_master(req_name):
    master = redis.Redis(host='localhost', port=master_server, db=0)
    data = master.get(req_name)
    master.incr(req_name+":lfu_count")
    # master.close()
    return data

def get_data_from_cache(port_num,req_name):
    r = redis.Redis(host='localhost', port=port_num, db=0)
    if not r.exists(req_name):
        # Get data from Master server in case it is not available        
        # print("GETTING DATA FROM MASTER PORT %s REQ_NAME %s" %(port_num,req_name))
        data = get_data_from_master(req_name)

        try:
            r.set(req_name,data)
        except:
            # This is triggered only when there is memory shortage
            while(not r.exists(req_name)):
                r.delete(req_name)
                evict_lfu(r)
                try:
                    # Check whether there is enough space now.
                    # If not evict again
                    r.set(req_name,data)
                except:
                    continue

        r.set(req_name+":lfu_count",0)
        
    else:
        data = r.get(req_name)

    r.incr(req_name+":lfu_count")
    # memory_stats = r.info(section="memory")
    # print("USED MEMORY", memory_stats["used_memory_human"])
    # print("MAX MEMORY", memory_stats["maxmemory_human"])
    # print()

    r.close()
    # print(data)
    return data

def evict_lfu(r):
    # r - redis object
    # memory_stats = r.info(section="memory")
    # print("USED MEMORY", memory_stats["used_memory_human"])
    # print("MAX MEMORY", memory_stats["maxmemory_human"])
    # print()

    counter_keys = [x.decode('ascii') for x in r.keys(pattern="*:lfu_count")]
    # print(counter_keys)
    counter_vals = [int(x.decode('ascii')) for x in r.mget(counter_keys)]
    # print(counter_vals)
    idx = np.argmin(counter_vals)
    key_rm = counter_keys[idx].replace(":lfu_count","")
    # print(key_rm)

    r.delete(counter_keys[idx],key_rm)
    # all_keys = [x.decode('ascii') for x in r.keys()]
    # all_keys.sort()
    # print(all_keys)
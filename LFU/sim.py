import threading
import redis
import time
from lfu import *

# def print_keys(r):
#     all_keys = [x.decode('ascii') for x in r.keys()]
#     all_keys.sort()
#     print(all_keys)

def simulate_requests(port_num,req_seq,reqtime_diff):
    data = []
    for i in range(len(req_seq)):
        time.sleep(reqtime_diff[i])
        data.append(get_data_from_cache(port_num,req_seq[i]))
    # print(data)
    return data


req_data = {
    "6380" : {
        "req_seq" : ['img1.jpeg','img1.jpeg', 'img1.jpeg', 'img1.jpeg', 'img1.jpeg','img1.jpeg', 'img1.jpeg','img1.jpeg','img1.jpeg', 'img11.jpeg','img11.jpeg','img11.jpeg','img11.jpeg','img11.jpeg','img15.png','img16.png','img17.png'],
        "reqtime_diff" : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    },
    "6381" : {
        "req_seq" : ['img1.jpeg','img1.jpeg', 'img1.jpeg', 'img1.jpeg', 'img1.jpeg','img1.jpeg', 'img1.jpeg','img1.jpeg','img1.jpeg', 'img11.jpeg','img11.jpeg','img11.jpeg','img11.jpeg','img11.jpeg','img15.png','img16.png','img17.png'],
        "reqtime_diff" : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    },
    "6382" : {
        "req_seq" : ['img1.jpeg','img1.jpeg', 'img1.jpeg', 'img1.jpeg', 'img1.jpeg','img1.jpeg', 'img1.jpeg','img1.jpeg','img1.jpeg', 'img11.jpeg','img11.jpeg','img11.jpeg','img11.jpeg','img11.jpeg','img15.png','img16.png','img17.png'],
        "reqtime_diff" : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    },
    "6383" : {
        "req_seq" : ['img1.jpeg','img1.jpeg', 'img1.jpeg', 'img1.jpeg', 'img1.jpeg','img1.jpeg', 'img1.jpeg','img1.jpeg','img1.jpeg', 'img11.jpeg','img11.jpeg','img11.jpeg','img11.jpeg','img11.jpeg','img15.png','img16.png','img17.png'],
        "reqtime_diff" : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    },
    "6384" : {
        "req_seq" : ['img1.jpeg','img1.jpeg', 'img1.jpeg', 'img1.jpeg', 'img1.jpeg','img1.jpeg', 'img1.jpeg','img1.jpeg','img1.jpeg', 'img11.jpeg','img11.jpeg','img11.jpeg','img11.jpeg','img11.jpeg','img15.png','img16.png','img17.png'],
        "reqtime_diff" : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    }
}

threads = []

for k,val in req_data.items():
    # print(k)
    # simulate_requests(k,val.req_seq,val.reqtime_diff)
    # print(val)
    t = threading.Thread(target=simulate_requests, args=(k,val["req_seq"],val["reqtime_diff"]))
    threads.append(t)

for t in threads:
    t.start()
    
for t in threads:
    t.join()

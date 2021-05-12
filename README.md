### FIRST TIME SETUP - 
Follow the following steps to setup redis server on your local PC. (Tested on Ubuntu 20.04)
https://redis.io/topics/quickstart
Add maxmemory to the above steps

Repeat the above procedure for different port number - 6380,6381,6382,6383,6384.

### STRUCTURE 
1 Main Server - MAXMEMORY : 20 MB - Port - 6379
5 Edge Servers/Users - MAXMEMORY : 4 MB - Port - 6380,6381,6382,6383,6384

### STARTING THE SERVER
sudo /etc/init.d/redis_6379 start
sudo /etc/init.d/redis_6380 start
sudo /etc/init.d/redis_6381 start
sudo /etc/init.d/redis_6382 start
sudo /etc/init.d/redis_6383 start
sudo /etc/init.d/redis_6384 start

To load all the data into the main server
```
python3 load.py
```

### LFU SYSTEM
``lfu.py`` implements Least Frequently Used Policy
To simulate one such case, you can use 
```
python3 sim.py
```

### STOPPING THE SERVER
sudo /etc/init.d/redis_6379 stop
sudo /etc/init.d/redis_6380 stop
sudo /etc/init.d/redis_6381 stop
sudo /etc/init.d/redis_6382 stop
sudo /etc/init.d/redis_6383 stop
sudo /etc/init.d/redis_6384 stop
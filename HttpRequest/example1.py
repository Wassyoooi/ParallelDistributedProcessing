# Example 1: synchronous requests
import requests
import time

start = time.time()

num_requests = 20

def http_get():
    requests.get('https://ie.u-ryukyu.ac.jp/')
    print(time.time() - start)

responses = [
    http_get()
    for i in range(num_requests)
]


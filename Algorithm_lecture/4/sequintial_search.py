class node:
    def __init__(self, key=None):
        self.key = key

class Dict:
    def __init__(self):
        self.a = []
    
    def search(self, search_key):
        i = 0
        n = len(Dict.a)
        while i <=n:
            if self.a[i].key == search_key:
                return i
            i += 1

        return -1

    def insert(self, v):
        Dict.a.append(node(v))

import random, time

N = 10000
key = list(range(1, N+1))
s_key = list(range(1, N+1))
random.shuffle(key)
d = Dict()

for i in range(N):
    d.insert(key[i])

start_time = time.clock()



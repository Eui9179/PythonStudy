import random

def random_arr(N, a=[]):
    a.append(None)
    for i in range(N):
        a.append(random.randint(1, N))
    
    return a
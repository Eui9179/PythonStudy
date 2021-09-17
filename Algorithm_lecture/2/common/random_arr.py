import random

def random_arr(a=[], N=1000):
    # a.append(None)
    for i in range(N):
        a.append(random.randint(0, N))
    
    return a
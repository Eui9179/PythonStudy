from common.random_arr import random_arr
from common.check_sort import checkSort
import time

def shell_sort(a, N):
    '''calculate h'''
    h = 0
    n = 0
    while h + (3**n) < len(a):
        h = h + 3**n
        n += 1
    n -= 1
    
    i = 1
    while h > 1:    
        if h + i <= N:
            if a[i] > a[h+i]:
                a[i], a[h+i] = a[h+i], a[i]
        else:
            h = h - 3**n
        i += 1
    
    for i in range(2, N+1):
        a[0] = a[i]
        j = i

        while j-1 != 0 and a[j-1] > a[0]:
            a[j] = a[j-1]    
            j -= 1

        a[j] = a[0]

    a[0] = None         
    return a

        
N = 10
a = random_arr(N=N)
print(a)

start_time = time.time()
a = shell_sort(a,N)
end_time = time.time() - start_time
print("선택 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))

checkSort(a, N)
print(a)
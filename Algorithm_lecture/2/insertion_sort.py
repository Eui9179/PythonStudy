from common.random_arr import random_arr
from common.check_sort import checkSort
import time

def insertion_sort(a, N):
    for i in range(2, N+1):
        a[0] = a[i]
        j = i

        while j-1 != 0 and a[j-1] > a[0]:
            a[j] = a[j-1]    
            j -= 1

        a[j] = a[0]
    return a

N = 1000
a = random_arr(N=N)

start_time = time.time()
a = insertion_sort(a, N)
end_time = time.time() - start_time

print("선택 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))

checkSort(a,N)
from common.check_sort import checkSort
from common.random_arr import random_arr
import time

def bubble_sort(a, N):
    for i in range(N, 1, -1):
        is_sorted = False
        for j in range(1 , i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                is_sorted = True

        if not is_sorted:
            break

    return a

N = 1000
a = random_arr()

'''performence'''
start_time = time.time()
bubble_sort(a, N)
end_time = time.time() - start_time
print("선택 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))

checkSort(a,N)
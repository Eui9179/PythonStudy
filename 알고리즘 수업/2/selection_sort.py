from common.random_arr import random_arr
from common.check_sort import checkSort

import time

def selection_sort(arr, N):

    for i in range(1,N):
        min_index = i

        for j in range(i+1, N+1):
            if arr[j] < arr[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

    return arr


N = 1000
a = []

random_arr(a, N)

'''performence'''
start_time = time.time()
selection_sort(a, N)
end_time = time.time() - start_time
print("선택 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))

'''정렬 성공 여부'''
checkSort(a, N)        
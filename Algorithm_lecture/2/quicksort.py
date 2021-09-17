from common.check_sort import checkSort
from common.random_arr import random_arr

import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    right_arr = []
    left_arr = []
    merged_arr = []
    for i in range(1,len(arr)):
        if arr[i] > pivot:
            right_arr.append(arr[i])
        
        else:
            left_arr.append(arr[i])

    merged_arr = merged_arr + quick_sort(left_arr) 
    merged_arr.append(pivot)
    merged_arr = merged_arr + quick_sort(right_arr)

    return merged_arr

a = []
arr = random_arr(a, 10000)

start_time = time.time()
checkSort(quick_sort(arr),len(arr)+1)
end_time = time.time() - start_time

print("선택 정렬의 실행 시간 : %0.3f"%(end_time))
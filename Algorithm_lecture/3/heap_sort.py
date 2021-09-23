from common.check_sort import checkSort
from common.random_arr import random_arr

def heap_sort(arr):
    length = len(arr) 
    for i in range(length // 2 - 1, -1, -1): 
        heapify(arr, i, length)
    for i in range(length - 1, 0 , -1): 
        arr[0], arr[i] = arr[i], arr[0] 
        heapify(arr, 0, i)

    return arr

def heapify(arr, index, heap_size):
    largest = index 
    left_index = 2 * index + 1 
    right_index = 2 * index + 2 

    if left_index < heap_size and arr[left_index] > arr[largest]: 
        largest = left_index 

    if right_index < heap_size and arr[right_index] > arr[largest]: 
        largest = right_index 

    if largest != index: 
        arr[largest], arr[index] = arr[index], arr[largest] 
        heapify(arr, largest, heap_size)


arr = random_arr(N=30)
checkSort(heap_sort(arr))
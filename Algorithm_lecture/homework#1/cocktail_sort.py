import random
import time

def checkSort(a, n):
    isSorted = True

    for i in range(0, n-1):
        if a[i] > a[i+1]:
            isSorted = False
        if not isSorted:
            break

    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")

def cocktail_shaker_sort(arr, N):
    switch = True
    start = 0
    end = N - 1
    
    while start <= N/2 <= end:

        if switch:
            for i in range(start, end):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            end -= 1

        else:
            for i in range(end, start, -1):
                if arr[i] < arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
            start += 1

        switch = not switch
       
    return arr


def myCocktailSort(arr, N):
    switch = True # 반향 바꾸는 변수
    start = 0 # 시작 범위
    end = N # 끝 범위
    index = 0 # 최댓값, 최솟값 index

    while start < N/2 < end: 
        if switch: # 최댓값 index 구하기
            for i in range(start, end):
                if arr[i] > arr[index]:
                    index = i # 최댓값의 index

            arr[index], arr[end-1] = arr[end-1], arr[index] # 최댓값과 범위안 맨 오른쪽 값과 교환
            end -= 1 # 끝 범위 - 1
            index = end - 1 # 다음 시작 index 

        else: # 최솟값 index 구하기
            for i in range(end, start-1, -1):
                if arr[i] < arr[index]:
                        index = i # 최솟값의 index

            arr[index], arr[start] = arr[start], arr[index] # 최솟값과 범위안 맨 왼쪽 값과 교환
            start += 1 # 시작 범위 + 1
            index = start # 다음 시작 index

        switch = not switch
       
    return arr

arr = []
N=10000

print('성능 향상 칵테일 정렬')

for i in range(N):
    arr.append(random.randint(0, N))

start_time = time.time()
a = myCocktailSort(arr,N)
end_time = time.time() - start_time

print("선택 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))

checkSort(arr, N)


            
        
import random, time

def selection_sort(arr, N):

    for i in range(1,N):
        min_index = i

        for j in range(i+1, N+1):
            if arr[j] < arr[min_index]:
                min_index = j

        tmp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = tmp

    return arr



def checkSort(a, n):
    isSorted = True

    for i in range(1, n):
        if a[i] > a[i+1]:
            isSorted = False
        if not isSorted:
            break

    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")


N = 10000
a = []

a.append(None)

for i in range(N):
    a.append(random.randint(1, N))


'''performence'''
start_time = time.time()
selection_sort(a, N)
end_time = time.time() - start_time
print("선택 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))

'''정렬 성공 여부'''
checkSort(a, N)        
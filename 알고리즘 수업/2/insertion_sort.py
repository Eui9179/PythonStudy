def insertion_sort(a, N):
    for i in range(1, N):
        a[0] = a[i]
        index = i
        for j in range(i-1,1,-1):
            if a[0] < a[j]:
                index = j
        a.insert(index, a[0])
        a[0] = None
    return a

a = [None,5,1,9,7,3,2,4,6,2,3]
N = 11

a

print(a)

print(insertion_sort(a,N))

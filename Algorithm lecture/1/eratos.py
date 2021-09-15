def eratos(a, n):
    a[1] = 0
    i = 2
    while i <= n/2:
        j = 2
        while i * j <= n:
            a[i*j] = 0
            j += 1
        i += 1 
    return a

n = int(input('배열 입력:'))
arr = list(range(n+1))

era = eratos(arr, n)

for a in arr:
    if a != 0:
        print(a)
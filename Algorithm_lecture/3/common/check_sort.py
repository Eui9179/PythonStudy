def checkSort(a, n=1000):
    isSorted = True

    for i in range(0, len(a)-1):
        if a[i] > a[i+1]:
            isSorted = False
        if not isSorted:
            break

    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")
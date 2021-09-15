def binarySearch(a, key, left, right):

    if left <= right:
        mid =int((left + right)/2)
        print("key={}, mid={}, left={}, right={}".format(key,mid,left,right))

        if key == a[mid]:
            print("key={}, mid={}".format(key,mid))
            return mid
        elif key < a[mid]:
            return binarySearch(a, key, left, mid-1)
        elif key > a[mid]:
            return binarySearch(a, key, mid+1, right)
    else:
        return -1

a=[]
for i in range(100):
    a.append(i)

key = int(input('key = '))
binarySearch(a,key,0,len(a))
def gcd(a, b):
    i = 1
    while i <= a and i <= b:
        if a % i == 0 and b % i == 0:
            g = i
        i += 1

    return g

a = int(input('a = '))
b = int(input('b = '))
print(gcd(a,b))

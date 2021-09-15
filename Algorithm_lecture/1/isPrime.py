def is_prime(a):
    i = 2;
    while i <= a/2:
        if a % i == 0:
            return False
        i += 1
    return True

a = int(input('a = '))

if is_prime(a):
    print("소수입니다.")
else:
    print("소수가 아닙니다.")
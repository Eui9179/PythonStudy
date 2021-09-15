def is_perfect(a):
    s = 0
    i = 2
    while i <= a/2 :
        if a % i == 0:
            s = s + 1;
        i += 1

    if s == a:
        return True

    return False

a = int(input('a = '))
if is_perfect(a):
    print('완전수 입니다.')
else:
    print('완전수가 아닙니다.')
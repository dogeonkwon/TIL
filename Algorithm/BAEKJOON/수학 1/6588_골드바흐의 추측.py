import sys


def prime(s):
    global a, b
    for k in range(2, int(s**(1/2)+1)):
        if s % k == 0:
            return 0
    return s


while True:
    n = int(sys.stdin.readline())
    if not n:
        break
    a = b = 0
    for i in range(3, n, 2):
        if prime(i):
            if prime(n-i):
                a = i
                b = n-i
                print(f'{n} = {a} + {b}')
                break
        if a and b:
            break
    if a and b:
        continue
    else:
        print('Goldbach\'s conjecture is wrong.')
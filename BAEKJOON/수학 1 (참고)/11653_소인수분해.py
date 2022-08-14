import sys

N = int(sys.stdin.readline().strip())

k = N // 2 + 1
m = 2

if N == 1:
    print()
else:
    while N > 1:
        if not N % m:
            N = int(N / m)
            print(m)
        else:
            m += 1
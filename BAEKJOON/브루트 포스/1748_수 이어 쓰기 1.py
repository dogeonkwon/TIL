import sys

n = int(sys.stdin.readline())
m = str(n)

if n < 10:
    print(n)
else:
    res = 9
    for i in range(len(m)-1, 0, -1):
        k = int('9' * i)
        res += (n-k) * (i+1)
        n -= (n-k)

    print(res)
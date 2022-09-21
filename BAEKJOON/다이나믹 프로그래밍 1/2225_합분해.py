import sys

n, k = map(int, sys.stdin.readline().split())

res = 1
v = n
m = 1.5

if n == 1:
    print(k % 1000000000)
else:
    a = (n - 2) / 2
    m += a
    for i in range(2, n+1):
        res += v
        v *= m
        if i == k:
            break
    print(res % 1000000000)
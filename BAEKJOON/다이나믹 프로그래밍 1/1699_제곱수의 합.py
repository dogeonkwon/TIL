import sys

n = int(sys.stdin.readline())
res = 0

while n >= 1:
    n = n - int(n**0.5)**2
    res += 1

print(res)
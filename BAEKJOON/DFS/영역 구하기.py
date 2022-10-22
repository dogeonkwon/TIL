import sys

m, n, k = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

for i in arr:
    print(i)
import sys, itertools

n, m = map(int, sys.stdin.readline().split())

arr = sorted(list(map(int, sys.stdin.readline().split())))

res = list(itertools.combinations(arr, m))

for i in res:
    print(*i)
import sys, itertools

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

res = sorted(list(set(itertools.permutations(arr, m))))

for i in res:
    print(*i)
import sys, itertools

n, m = map(int, sys.stdin.readline().split())
lst = sorted(list(map(int, sys.stdin.readline().split())))

res = list(itertools.permutations(lst, m))

for i in res:
    print(*i)
import sys, itertools

n, m = map(int, sys.stdin.readline().split())
res_lst = [0] * n
for i in range(n):
    res_lst[i] = i + 1
ans = list(itertools.permutations(res_lst, m))
for j in ans:
    print(*j)

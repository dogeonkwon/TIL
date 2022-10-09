import sys, itertools

n, m = map(int, sys.stdin.readline().split())

sub = [0] * n
for i in range(n):
    sub[i] = i+1
res = list(itertools.combinations_with_replacement(sub, m))

for j in res:
    print(*j)
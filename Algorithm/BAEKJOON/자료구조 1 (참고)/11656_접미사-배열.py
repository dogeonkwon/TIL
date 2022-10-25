import sys

S = sys.stdin.readline().strip()
ans = list()
n = len(S)
for i in range(n):
    ans.append(S[i:n])
ans.sort()
for j in ans:
    print(j)
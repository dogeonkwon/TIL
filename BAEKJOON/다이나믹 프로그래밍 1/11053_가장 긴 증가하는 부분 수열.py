import sys

n = int(sys.stdin.readline())

dp = sorted(list(map(int, sys.stdin.readline().split())))
res = 1

for i in range(1, n):
    if dp[i] > dp[i-1]:
        res += 1

print(res)
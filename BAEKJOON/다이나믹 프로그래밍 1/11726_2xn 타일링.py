import sys

n = int(sys.stdin.readline())

dp = [0] * (n+2)    # n이 1 or 2 일 때를 위해서 n + 2
dp[1] = 1
dp[2] = 2

# 피보나치 수열
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)
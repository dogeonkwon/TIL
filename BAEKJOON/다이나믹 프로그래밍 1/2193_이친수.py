import sys

# dp[n] = dp[i-1] + dp[i-2] 법칙(귀납법)
n = int(sys.stdin.readline())
dp = [0, 1, 1] + [0]*n

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
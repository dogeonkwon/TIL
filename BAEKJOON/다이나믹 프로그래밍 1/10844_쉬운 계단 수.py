import sys

n = int(sys.stdin.readline())

dp = [0] * (n+1)
dp[1] = 9

# n = n*2 - (n-1)
# 1 => 9
# 2 => 17
# 3 => 32
for i in range(2, n+1):
    dp[i] = dp[i-1]*2 - (i-1)

print(dp[n] % 1000000000)
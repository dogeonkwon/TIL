import sys

N = int(sys.stdin.readline())

arr = [0] * (N+1)

for i in range(2, N+1):
    arr[i] = arr[i-1] + 1

    if arr[i]



















# N = int(sys.stdin.readline().strip())
#
# dp = [0 for _ in range(N+1)]
#
#
# dp[1] = 0
# for i in range(2, N+1):
#     dp[i] = dp[i-1] + 1
#
#     if i % 3 == 0 and dp[i//3] + 1 < dp[i]:
#         dp[i] = dp[i//3] + 1
#     if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
#         dp[i] = dp[i//2] + 1
#
# print(dp[N])
import sys

n, k = map(int, sys.stdin.readline().split())

dp = [[0]*201 for _ in range(201)]

# 행이 k를 나타내고 열이 n을 나타냄
# dp[2][i]는 k = 2이고 n = i 일 때 값을 구하는 것
for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i+1

for j in range(2, 201):
    dp[j][1] = j
    for l in range(2, 201):
        dp[j][l] = (dp[j][l-1] + dp[j-1][l]) % 1000000000

print(dp[k][n])
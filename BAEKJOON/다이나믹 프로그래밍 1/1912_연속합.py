import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 연속된 숫자들의 최대 합
dp = [0] * n
dp[0] = arr[0]

# 이전 숫자들의 최대 합(dp[i-1])이 양수라면 현재 숫자(arr[i])와 더해준다.
# 이외는 그냥 자기자리로..
for i in range(1, n):
    if dp[i-1] > 0:
        dp[i] = dp[i-1] + arr[i]
    else:
        dp[i] = arr[i]

print(max(dp))
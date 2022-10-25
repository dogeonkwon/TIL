import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = 1

# 가장 긴 증가하는 부분 수열 dp에 정리
for i in range(1, n):
    for j in range(i):
        if dp[j] > dp[i] and arr[j] < arr[i]:
            dp[i] = dp[j]
    dp[i] += 1

# 길이가 가장 긴 수열의 자리 확인
max_idx = dp.index((max(dp)))
# 임의의 값에 저장
tmp = max_idx
# 결과를 저장할 리스트
res = [arr[max_idx]]

# 뒤에서부터 가장 큰 길이 - 1 한 것의 dp값을 확인 후 res에 저장
for k in range(max_idx-1, -1, -1):
    if dp[k] == dp[tmp] - 1:
        res.append(arr[k])
        tmp = k

print(max(dp))
res.reverse()
print(*res)
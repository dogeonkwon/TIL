import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n

res = [[] for _ in range(n)]
tmp = 0
ans = []

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1
    if dp[i] == 1:
        res[tmp].append(arr[i])
        tmp += 1
    else:
        for k in range(n):
            if res[k] == []:
                break
            elif res[k][-1] < arr[i]:
                res[k].append(arr[i])
                if len(res[k]) > len(ans):
                    ans = res[k]

print(len(ans))
print(*ans)
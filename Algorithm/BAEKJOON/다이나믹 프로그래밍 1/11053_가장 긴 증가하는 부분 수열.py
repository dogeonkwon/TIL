import sys
input = sys.stdin.readline

n = int(input())
dp = list(map(int, input().split()))

res = [0] * n

# 현재 수열의 수가 이전 수열들 보다 숫자가 크다면 가장 res값이 큰 수에 +1을 하여 저장해줌
for i in range(n):
    for j in range(i):
        if dp[i] > dp[j] and res[i] < res[j]:
            res[i] = res[j]
    res[i] += 1

print(max(res))



# # 주어진 수열에서 제일 작은 수에서 제일 큰수로 몇 개의 수가 있는지 체크한거
# # 수열의 순서를 바꾸면 안되는 문제였음
# import sys
#
# n = int(sys.stdin.readline())
#
# dp = sorted(list(map(int, sys.stdin.readline().split())))
# res = 1
#
# for i in range(1, n):
#     if dp[i] > dp[i-1]:
#         res += 1
#
# print(res)
import sys

t = int(sys.stdin.readline())





























































# import sys
#
# t = int(sys.stdin.readline())
#
# # 3,4개 정도를 직접 풀어보면서 규칙을 찾고 점화식을 만들기
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     dp = [0, 1, 2, 4] + ([0] * n)
#
#     for i in range(4, n+1):
#         dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
#
#     print(dp[n])
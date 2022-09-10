import sys

# 2차원 배열로 생각하여 풀이
# [총합, 1로 끝난 경우, 2로 끝난 경우, 3으로 끝난 경우]

# 1, 2, 3 이 후의 값들은 -1개 전의 총합에서 1로 끝나지 않은 경우를 더해주면 된다.
# -2개 전의 총합에서 2로 끝나지 않은 경우들을 더해주고
# -3개 전의 총합에서 3으로 끝나지 않은 경우들을 더해준다.
dp = [[0, 0, 0, 0] for _ in range(100001)]

dp[1] = [1, 1, 0, 0]
dp[2] = [1, 0, 1, 0]
dp[3] = [3, 1, 1, 1]


# 예를 들어 dp[4]의 총합은
# [?, dp[4-1]에서 1로 끝나지 않은 경우들의 합, dp[4-2]에서 2로 끝나지 않은 경우들의 합, dp[4-3]에서 3으로 끝나지 않은 경우들의 합]
# 따라서 ?는 3이 된다.
for i in range(4, 100001):
    total = 0
    for j in range(1, 4):
        dp[i][j] = dp[i-j][0] - dp[i-j][j]
        total += dp[i][j]

    # 총합에 % 1000000009를 안하면 메모리 초과가 난다.
    dp[i][0] = total % 1000000009

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n][0])


# import sys
#
# t = int(sys.stdin.readline())
#
# for _ in range(t):
#     n = int(sys.stdin.readline())
#
#     # 세 가지 규칙을 생각함
#     # 1 2 3 | 4 5 6 | 7 8 9 | 10
#     # 1 1 3 | 3 4 8 | 9 13 23 | 27
#     if n % 3 == 1:
#         m = n // 3
#         print(3**m % 1000000009)
#     elif n % 3 == 2:
#         m = n // 3
#         k = 3**m
#         print((k + k//2) % 1000000009)
#     else:
#         m = n // 3
#         k = 3**m // 3 // 2
#         print((3**m - k) % 1000000009)

import sys

n = int(sys.stdin.readline())

res = [0] + [1]*9

#          각 자리수에서 맨 뒤에 올수 있는 숫자의 개수(0~9)
#            0  1  2  3  4  5  6  7  8  9
# 자리수(1)   0  1  1  1  1  1  1  1  1  1
# 자리수(2)   1  1  2  2  2  2  2  2  2  1
# 자리수(3)   1  3  3  4  4  4  4  4  3  2

# 해당 위치의 왼쪽, 오른쪽 대각선 숫자들의 합인 걸 알 수 있음
for i in range(2, n+1):
    tmp = [0] * 10
    for j in range(10):
        if 0 < j < 9:
            tmp[j] = res[j-1] + res[j+1]
        elif j == 0:
            tmp[j] = res[1]
        else:
            tmp[j] = res[8]
    res = tmp

print(sum(res) % 1000000000)


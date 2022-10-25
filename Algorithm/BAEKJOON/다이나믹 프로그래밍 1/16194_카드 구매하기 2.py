import sys

n = int(sys.stdin.readline())
pack = [0] + list(map(int, sys.stdin.readline().split()))

# min_num[0]도 999999999999 로 잡고 하여 실수를 했음
min_num = [0, pack[1]] + [999999999999] * (n-1)

# min_num[1] = pack[1]
# min_num[2] = min(min_num[1] + pack[1], pack[2])
# min_num[3] = min(min_num[2] + pack[1], min_num[1] + pack[2], pack[3])
# min_num[4] = min(min_num[3] + pack[1], min_num[1] + pack[3], min_num[2] + pack[2], pack[4])
for i in range(2, n+1):
    for j in range(1, i+1):
        if min_num[i] > min_num[i-j] + pack[j]:
            min_num[i] = min_num[i-j] + pack[j]

print(min_num[n])
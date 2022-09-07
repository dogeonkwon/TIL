import sys

n = int(sys.stdin.readline())

# 최대값과 인덱스를 같이 비교하기 위해 앞에 [0] 추가
pack = [0] + list(map(int, sys.stdin.readline().split()))
max_num = [0] * (n + 1)

max_num[1] = pack[1]

# max_num[1] = pack[1]
# max_num[2] = max(pack[2], max_num[1] + pack[1])
# max_num[3] = max(pack[3], max_num[2] + pack[1], max_num[1] + pack[2])
# max_num[4] = max(pack[4], max_num[3] + pack[1], max_num[1] + pack[3], max_num[2] + pack[2])
for i in range(2, n+1):
    for j in range(1, i+1):
        if max_num[i] < max_num[i-j] + pack[j]:
            max_num[i] = max_num[i-j] + pack[j]

print(max_num[n])
import sys

# 미래에서 사용하는 A진법 / 정이가 사용하는 B진법
A, B = map(int, sys.stdin.readline().split())

# A진법으로 나타낸 숫자의 자리수의 개수
m = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))[::-1]

numA = 0

# A진법을 이루고 있는 숫자 m개가 공백을 구분으로 높은 자릿수부터 차례대로 주어진다.
res = list()

for i in range(len(nums)):
    numA += nums[i] * (A**i)

while numA != 0:
    res.append(numA % B)
    numA //= B

print(" ".join(map(str, res[::-1])))
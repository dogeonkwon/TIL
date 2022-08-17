import sys

A, B = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))[::-1]

numA = 0
res = list()

for i in range(len(nums)):
    numA += nums[i] * (A**i)

while numA != 0:
    res.append(numA % B)
    numA //= B

print(" ".join(map(str, res[::-1])))
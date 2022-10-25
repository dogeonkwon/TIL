import sys

tc = int(sys.stdin.readline().strip())

nums = [0] * tc
maxNum = 4
for l in range(tc):
    nums[l] = int(sys.stdin.readline().strip())

    if maxNum < nums[l]:
        maxNum = nums[l]

prime = [True] * (maxNum + 1)

for i in range(2, int(maxNum**0.5 + 1)):
    if prime[i]:
        for j in range(i+i, maxNum + 1, i):
            prime[j] = False

for n in nums:
    ans = 0
    for m in range(2, n//2 + 1):
        if prime[m] and prime[n-m]:
            ans += 1
    print(ans)
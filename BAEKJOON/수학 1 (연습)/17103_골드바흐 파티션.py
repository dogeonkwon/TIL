import sys

tc = int(sys.stdin.readline())

nums = [0] * tc
maxN = 0
for l in range(tc):
    k = int(sys.stdin.readline())
    nums[l] = k

    if maxN < k:
        maxN = k

prime = [True] * (maxN + 1)
prime[1] = False

for i in range(2, int(maxN ** 0.5) + 1):
    if prime[i]:
        for j in range(i + i, maxN + 1, i):
            prime[j] = False

for n in nums:
    ans = 0
    for m in range(2, n // 2 + 1):
        if prime[m] and prime[n - m]:
            ans += 1

    print(ans)

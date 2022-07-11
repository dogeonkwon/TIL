import sys


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


t = int(sys.stdin.readline())
for _ in range(t):
    ans = 0
    lst = list(map(int, sys.stdin.readline().split()))
    for i in range(1, lst[0]):
        for j in range(i+1, lst[0]+1):
            ans += gcd(lst[i], lst[j])
    print(ans)
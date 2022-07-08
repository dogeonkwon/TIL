import sys

def prime(s):
    global ans
    if s < 2:
        return
    elif int(s**(1/2)) <= 2:
        if s % 2 == 0:
            return
    for i in range(2, int(s**(1/2))+1):
        if s % i == 0:
            return
    ans += 1
    return


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
ans = 0

for i in range(n):
    if a[i] == 2:
        ans += 1
    else:
        prime(a[i])
print(ans)
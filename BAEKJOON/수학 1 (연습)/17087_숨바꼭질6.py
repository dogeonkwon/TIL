import sys


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n, s = map(int, sys.stdin.readline().split())
brother = list(map(int, sys.stdin.readline().split()))
distance = list()
ans = 0
if n >= 2:
    for i in range(n):
        distance.append(abs(s-brother[i]))
    for _ in range(n):
        distance.append(gcd(distance.pop(), distance.pop()))
        if len(distance) == 1:
            print(distance[0])
            break
else:
    print(abs(s - brother[0]))
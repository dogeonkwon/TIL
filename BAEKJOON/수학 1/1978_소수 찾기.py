import sys

def prime(n):
    if n < 2:
        return False
    for i in range(n):
        if n % i == 0:
            return False
    return True


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    prime(a[i])
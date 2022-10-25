import sys

def prime(s):
    if s < 2:
        return
    elif int(s**(1/2)) < 2:
        if s % 2 == 0:
            return
    for j in range(2, int(s**(1/2))+1):
        if s % j == 0:
            return
    print(s)


M, N = map(int, sys.stdin.readline().split())

for i in range(M, N+1):
    if i == 2:
        print(i)
    else:
        prime(i)
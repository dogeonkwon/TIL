import sys

t = int(sys.stdin.readline())
for _ in range(t):
    k = 0
    m, n, x, y = map(int, sys.stdin.readline().split())
    i = j = 0
    stop = 1
    while stop:
        i = (i % m) + 1
        j = (j % n) + 1
        k += 1

        if i == x:
            if j == y:
                print(k)
                stop = 0
                break

        if i == m:
            if j == n:
                print(-1)
                stop = 0
                break

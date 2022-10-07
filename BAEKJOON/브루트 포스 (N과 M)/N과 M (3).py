import sys


def pick(n, bucket, k):
    if k == 0:
        print(*bucket)
        return

    lastIdx = len(bucket) - k - 1
    smallest = 1

    for i in range(smallest, n+1):
        bucket[lastIdx + 1] = i
        pick(n, bucket, k-1)


n, m = map(int, sys.stdin.readline().split())
pick(n, [0]*m, m)
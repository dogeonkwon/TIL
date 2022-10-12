import sys


def pick(n, bucket, k):
    global arr

    if k == 0:
        print(*bucket)
        return

    lastidx = len(bucket) - k

    for i in range(0, n):
        bucket[lastidx] = arr[i]
        pick(n, bucket, k-1)


n, m = map(int, sys.stdin.readline().split())

arr = sorted(list(map(int, sys.stdin.readline().split())))

pick(n, [0]*m, m)
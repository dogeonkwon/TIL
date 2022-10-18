import sys, itertools

def pick(n, bucket, k):
    global m, arr

    if k == 0:
        print(*bucket)
        return

    lastidx = len(bucket) - k

    for i in range(0, len(arr)):
        bucket[lastidx] = arr[i]
        pick(n, bucket, k-1)


n, m = map(int, sys.stdin.readline().split())

arr = sorted(set(map(int, sys.stdin.readline().split())))

pick(n, [0]*m, m)
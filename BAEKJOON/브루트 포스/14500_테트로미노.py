import sys, collections

n, m = map(int, sys.stdin.readline().split())

arr = list(list(map(int, sys.stdin.readline().strip().split())) for _ in range(n))

res = 0
for i in range(n):
    for j in range(m):
         q = collections.deque([[[i, j]]])

         while q:
             v = q.popleft()
             print(v)
             if len(v) == 4:
                 if arr[v[0][0]][v[0][1]] + arr[v[1][0]][v[1][1]] + arr[v[2][0]][v[2][1]] + arr[v[3][0]][v[3][1]] > res:
                     res = arr[v[0][0]][v[0][1]] + arr[v[1][0]][v[1][1]] + arr[v[2][0]][v[2][1]] + arr[v[3][0]][v[3][1]]
             for k in (0, 1), (1, 0), (0, -1), (-1, 0):
                 v[]
import sys, collections


def bfs(x, y):
    global sub

    q = collections.deque([[x, y]])

    while q:
        v = q.popleft()
        for i, j in (0, 1), (1, 0), (0, -1), (-1, 0):
            xx = v[0] + i
            yy = v[1] + j
            if 0 <= xx < m and 0 <= yy < n:
                if not res[xx][yy]:
                    res[xx][yy] = 1
                    sub += 1
                    q.append([xx, yy])


m, n, k = map(int, sys.stdin.readline().split())

res = [[0 for _ in range(n)] for _ in range(m)]

ans = list()

# 빈칸 색칠
for _ in range(k):
    coordinate = list(map(int, sys.stdin.readline().split()))
    for i in range(m-coordinate[3], m-coordinate[1]):
        for j in range(coordinate[0], coordinate[2]):
            res[i][j] = 1

# 색칠안된 빈칸 구하기
for i in range(m):
    for j in range(n):
        if not res[i][j]:
            sub = 1
            res[i][j] = 1
            bfs(i, j)
            ans.append(sub)

ans.sort()
print(len(ans))
print(*ans)

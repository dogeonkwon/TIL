import sys

def dfs(a, b, c, d):
    global res

    for x, y in (0, 1), (-1, 0):
        xx = a + x
        yy = b + y
        if c <= xx <= a and b <= yy <= d:
            res[xx][yy] = 1
            dfs(xx, yy, c, d)


def dfs2(x, y):
    global sub

    for i, j in (0, 1), (1, 0), (0, -1), (-1, 0):
        xx = x + i
        yy = y + j
        if 0 <= xx < m and 0 <= yy < n:
            if not res[xx][yy]:
                res[xx][yy] = 1
                sub += 1
                dfs2(xx, yy)


m, n, k = map(int, sys.stdin.readline().split())

res = [[0 for _ in range(n)] for _ in range(m)]

ans = list()

for _ in range(k):
    coordinate = list(map(int, sys.stdin.readline().split()))
    a = m - coordinate[1] - 1
    b = coordinate[0]
    c = m - coordinate[3]
    d = coordinate[2] - 1
    res[a][b] = 1
    dfs(a, b, c, d)

for i in range(m):
    for j in range(n):
        if not res[i][j]:
            sub = 1
            res[i][j] = 1
            dfs2(i, j)
            ans.append(sub)

print(len(ans))
print(sorted(ans))

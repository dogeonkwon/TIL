import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0 for _ in range(M)] for _ in range(N)]
check = [[0 for _ in range(M)] for _ in range(N)]
max_val = 0
for i in range(N):
    row = list(map(int, input().split()))
    for j, r in enumerate(row):
        graph[i][j] = r
        if max_val < r:
            max_val = r

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

sol = 0


def dfs(y, x, depth, s):
    global sol
    if depth == 4:
        sol = max(s, sol)
        return False
    if s + (4 - depth) * max_val <= sol:
        return False  # 나머지 깊이 값이 모두 최대값이라도 갱신 불가능한 경우
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < N and 0 <= nx < M and check[ny][nx] == 0:
            if depth == 2:  # 'ㅏ', 'ㅓ' 모양의 가운데 지점인 경우 (깊이 2)
                check[ny][nx] = 1  # 깊이 3의 지점 방문 처리
                # 깊이 2 지점에서 다시 탐색해서 깊이 4 지점 탐색
                dfs(y, x, depth + 1, s + graph[ny][nx])
                check[ny][nx] = 0
            check[ny][nx] = 1
            dfs(ny, nx, depth + 1, s + graph[ny][nx])
            check[ny][nx] = 0
    return False


for i in range(N):
    for j in range(M):
        check[i][j] = 1
        dfs(i, j, 1, graph[i][j])
        check[i][j] = 0
print(sol)
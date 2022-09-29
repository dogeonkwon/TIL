import sys, collections

def BFS(start, visited):

    q = collections.deque([start])
    visited[start] = 1

    while q:
        v = q.popleft()

        if v == k:
            print(visit[k]-1)
            break

        for i in (v+1, v-1, v*2):
                if 0 <= i <= 100000 and not visit[i]:
                    visit[i] = visit[v] + 1
                    q.append(i)

n, k = map(int, sys.stdin.readline().split())
visit = [0] * 100001
BFS(n, visit)



# def DFS(cnt, v, visited):
#     global res
#
#     if cnt >= res or 0 > v or 100000 < v:
#         return
#
#     if v == k:
#         res = cnt
#         return
#
#     for i in (v-1, v+1, v*2):
#         if visited[i] > cnt:
#             visited[v] = cnt
#             DFS(cnt+1, i, visited)
#
# n, k = map(int, sys.stdin.readline().split())
# visit = [99999999] * 100001
# res = 99999999
# DFS(0, n, visit)
# print(res)


# 14
# 14
# 11
# 8
# 7
# 7
# 5
# 4
# 4



# 14
# 11
# 8
# 7
# 5
# 4
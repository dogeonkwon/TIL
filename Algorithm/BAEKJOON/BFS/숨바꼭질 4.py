# from collections import deque
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
# n,k = map(int,input().split())
# MAX_INDEX = 100000
# board = [MAX_INDEX] * (MAX_INDEX+1)
# move_to = [0] * (MAX_INDEX + 1)
# q = deque()
# q.append(n)
# board[n] = 0
# while q:
#     x = q.popleft()
#     if x == k:
#         break
#     for nx in (x-1, x+1, x*2):
#         if 0 <= nx <= MAX_INDEX and board[nx] == MAX_INDEX:
#             q.append(nx)
#             board[nx] = board[x] + 1
#             move_to[nx] = x
#
# def move(n,m):
#     if n != m:
#         move(n,move_to[m])
#     print(m, end=' ')
#
# print(board[k])
# move(n,k)



import itertools

arr = [2, 3, 6, 8, 4, 1, 5, 9]

arr.pop(3)
arr.insert(1, 2)
# arr.remove(3)
print(arr)
# [2, 3, 6, 4, 2, 1, 5, 9]
# [2, 3, 6, 4, 1, 5, 9, 2]

# print(list(itertools.permutations(arr, 3)))
# print(list(itertools.combinations(arr, 3)))
# print(list(itertools.combinations_with_replacement(arr, 2)))



# import sys, collections
#
# def graph_path(start, end):
#     if start != end:
#         graph_path(start, graph[end])
#     if end == k:
#         print(end)
#     else:
#         print(end, end=' ')
#
#
# n, k = map(int, sys.stdin.readline().split())
#
# visited = [0] * 100001
# graph = [0] * 100001
#
# q = collections.deque([n])
# visited[n] = 1
#
# while q:
#     v = q.popleft()
#
#     if v == k:
#         print(visited[v] - 1)
#         break
#
#     for i in (v-1, v+1, v*2):
#         if not visited[i] and 0 <= i <= 100000:
#             q.append(i)
#             visited[i] = visited[v] + 1
#             graph[i] = v
#
# graph_path(n, k)

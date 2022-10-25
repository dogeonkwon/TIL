# 4871_그래프-경로 풀이
# 2022-02-22


import sys
sys.stdin = open('sample_input.txt', 'r')


# def dfs(s, g):            # 깊이우선탐색 함수 구현
#
#     visited.append(s)
#     for i in range(E):
#         if first[i] == s:
#             visited.append(ends[i])
#             stack.append(ends[i])
#     while stack:
#         now = stack.pop()
#         for j in range(E):
#             if first[j] == now and ends[j] not in visited:
#                 visited.append(ends[j])
#                 stack.append(ends[j])
#     for k in visited:
#         if k == g:
#             return 1
#     return 0


T = int(input())

for tc in range(1, T+1):

    V, E = map(int, input().split())    # V = 노드 수, E = 간선 수
    first = list()                  # 시작 값들을 모아둠
    ends = list()                   # 도착 값들을 모아둠
    visited = list()                # 방문한 값들을 저장
    stack = list()                  # 지나간 경로를 나타냄(pop할 수 있음)
    result = 0                      # 결국 방문한 곳중(visited)에서 찾고자 하는 값이 있으면 1로 바꿔줌

    for _ in range(E):
        v, e = map(int, input().split())     # 시작 값들과 도착 값들을 받으면서 나눠줌
        first += [v]
        ends += [e]

    S, G = map(int, input().split())        # S = 출발노드, G = 도착노드

    visited += [S]                          # visited에 시작값을 추가하면서 탐색시작
    for i in range(E):                      # E개만큼 정보가 주어졌으니 E만큼 반복문을 돌리면서 시작값과 같은 출발값을 가지는 끝값들을 visited와 stack에 저장해줌
        if first[i] == S:
            visited += [ends[i]]
            stack += [ends[i]]

    while stack:                            # stack이 없어질때까지 탐색
        now = stack.pop()                   # stack의 가장 마지막값을 뽑아낸다.
        for j in range(E):                  # 가장 마지막값을 출발점으로 가지는 끝값들을 찾아준다.(단, 이전에 방문하지 않아야 하는 값들이어야 하므로 not in visited라는 조건이 붙는다.)
            if first[j] == now and ends[j] not in visited:
                visited += [ends[j]]
                stack += [ends[j]]

    for k in visited:                       # visited에서 G(목표값)와 같은 값이 있다면 성공!
        if k == G:
            result = 1

    print('#{} {}'.format(tc, result))



    # 함수로 구현했을 때는 밑에 것들을 S, G 바로 밑의 코드를 아래 2줄 코드로 대체하면 된다.
    # result = dfs(S, G)
    # print('#{} {}'.format(tc, result))

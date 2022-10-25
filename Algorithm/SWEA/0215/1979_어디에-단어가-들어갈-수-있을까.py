# 1979_어디에-단어가-들어갈-수-있을까 풀이
# 2022-02-15


import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T + 1):

    # N은 열과 행의 길이, M은 주어진 글자의 길이
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 조건에 맞다면 cnt를 하나씩 올려준다.
    cnt = 0

    # 조건에 맞는 열의 개수 구하기
    for i in range(N):

        # 새로운 열을 탐색할 때마다 total을 초기화 시켜준다.
        total = 0

        for j in range(N):

            # 시작하는 곳의 숫자가 1이어야 하고 total에 +1을 해준다
            if arr[i][j] == 1:
                total += 1

            # 그러다 다음 숫자가 0이라면 다시 초기화 시켜주기 위하여 total을 0으로 잡아준다.
            elif arr[i][j] == 0:
                total = 0

            # 한 열을 돌다가 total의 수가 M과 같을 때
            # 뒤에 더 들어올 숫자가 없다면(j+1 == N 이라면 범위에서 벗어나므로 끝자리임, arr[i][j+1] == 0 이라면 일단 빈칸이 끝난다는 의미)
            # 모든 조건이 성립한다면 cnt += 1
            if total == M and (j + 1 == N or arr[i][j+1] == 0):
                cnt += 1

    # 조건에 맞는 행의 개수 구하기
    for k in range(N):

        # 새로운 행을 탐색할 때마다 total을 초기화 시켜준다.
        total = 0

        for l in range(N):

            # 시작하는 곳의 숫자가 1이어야 하고 total에 +1을 해준다
            if arr[l][k] == 1:
                total += 1

            # 그러다 다음 숫자가 0이라면 다시 초기화 시켜주기 위하여 total을 0으로 잡아준다.
            elif arr[l][k] == 0:
                total = 0

            # 한 행을 돌다가 total의 수가 M과 같을 때
            # 뒤에 더 들어올 숫자가 없다면(j+1 == N 이라면 범위에서 벗어나므로 끝자리임, arr[i][j+1] == 0 이라면 일단 빈칸이 끝난다는 의미)
            # 모든 조건이 성립한다면 cnt += 1
            if total == M and (l + 1 == N or arr[l+1][k] == 0):
                cnt += 1

    print('#{} {}'.format(tc, cnt))

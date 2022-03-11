# 1954_달팽이-숫자 풀이
# 2022-02-14


import sys
sys.stdin = open('input.txt', 'r')


T = int(input())


for tc in range(1, T + 1):

    N = int(input())

    # N의 길이에 맞는 0을 담은 리스트를 만들어 준다.
    lst = [[0 for _ in range(N)] for _ in range(N)]

    # 방향을 조절하기 위해 오른쪽, 아래, 왼쪽, 위 순으로 움직을 수 있도록 dr, dc를 만들어준다.
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 초기 인덱스 r, c는 0을 가진다.
    r = c = 0

    # control은 0이면 오른쪽, 1이면 아래, 2이면 왼쪽, 3이면 위로 움직을 수 있도록 해준다.
    control = 0

    # 가로와 세로의 곱에 + 1 까지 숫자를 넣는다.
    for num in range(1, N*N+1):

        # 초기 lst[0][0]에 num 값을 넣고 시작한다.
        lst[r][c] = num

        # 주어진 조건에서 벗어나지 않는다면 계속 오른쪽, 그 다음 아래, 왼, 위 순으로 움직일 수 있도록 고정 시켜준다.
        r += dr[control]
        c += dc[control]

        # 그러다 만약 이 조건을 만족할 시 다시 정상적으로 움직일 수 있도록 수정해준다.
        # r, c가 0보다 작거나 N보다 크거나 같을 경우 인덱스를 벗어난다. 또한 lst[r][c]가 0이 아닌 경우에는 이미 숫자가 있다는 의미이므로 다른 경로를 탐색하도록 한다.
        if r < 0 or r >= N or c < 0 or c >= N or lst[r][c] != 0:


            # 우선 갔던 경로를 다시 돌아오도록 만든다.
            r -= dr[control]
            c -= dc[control]

            # 그 뒤 방향을 바꿔주는 contorl에 +1을 한 뒤 % 4를 해주면 90도 방향을 돌리게 된다.
            control = (control + 1) % 4

            # 위 과정이 끝났다면 다시 제대로 된 방향으로 움직일 수 있도록 한다.
            r += dr[control]
            c += dc[control]


    # 이 과정이 끝났다면 출력을 해준다.
    print('#{}'.format(tc))

    # lst의 행들을 뽑아낸다.
    for i in lst:

        # 뽑아낸 행의 숫자들을 하나씩 여백을 이어서 출력하는데 만약  j와 i의 마지막 값이 같아지면 뒤에 여백이 붙지 않도록 그냥 j만 출력한다.
        # 그렇게 하면 자동으로 줄바꿈도 일어남
        for j in i:
            if j == i[-1]:
                print(j)
            else:
                print(j, end=' ')

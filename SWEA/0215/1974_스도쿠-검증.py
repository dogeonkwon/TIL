# 1974_스도쿠-검증 풀이
# 2022-02-15


import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T+1):

    arr = [list(map(int, input().split())) for _ in range(9)]

    # 한 줄에는 1~9까지의 숫자가 하나씩 있어야 하므로 비교하기 위한 서브 리스트를 만들어준다.
    sub_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # fail이 1개라도 생긴다면 실패한 것으로 간주
    fail = 0

    # result의 기본값을 0으로 잡는다
    result = 0

    # 행, 열에서 중복된 값이 있는지 확인하기 위한 반복문
    # sub_lst에 있는 값을 순서대로 출력하여 각 행과 열에 몇 번 나오는 지 확인한다.
    for i in sub_lst:
        for j in range(9):

            # 행의 중복값을 카운트
            overlap_r = 0
            # 열의 중복값을 카운트
            overlap_c = 0

            for k in range(9):

                # 불필요한 연산을 하지 않도록 overlap_r이 2이상이 되면 바로 반복문을 종료하도록 한다.
                if i == arr[j][k]:
                    overlap_r += 1
                if overlap_r >= 2:
                    fail += 1
                    break

                # 불필요한 연산을 하지 않도록 overlap_c가 2이상이 되면 바로 반복문을 종료하도록 한다.
                if i == arr[k][j]:
                    overlap_c += 1
                if overlap_c >= 2:
                    fail += 1
                    break

        # 여기서도 불필요한 연산을 하지 않도록 fail이 이미 나왔다면 식을 모두 종료하기 위해 break를 넣는다.
        if fail >= 1:
            break

    # 9칸에 있는 숫자들의 중복된 값을 확인하는 반복문
    for i in range(0, 9, 3):

        # 여기서도 불필요한 연산을 하지 않도록 fail이 이미 나왔다면 식을 모두 종료하기 위해 break를 넣는다.
        if fail >= 1:
            break

        # 각 시작지점을 열을 3씩 혹은 행이 3씩 증가한 후 설정하였다.
        # (0, 0), (0, 3), (0, 6)과 같이 3씩 늘어남
        for j in range(0, 9, 3):

            # 시점지점으로부터 조건에 맞는 범위에 있는 숫자들을 담을 리스트
            lst = []

            # 시작지점으로부터 3x3 범위의 값을 lst에 담아준다.
            for k in range(3):
                for l in range(3):
                    lst += [arr[i+k][j+l]]

            # lst에 있는 값들을 하나씩 빼서 겹치는 것이 있는 확인한다.
            for n in lst:
                overlap = 0
                for m in range(9):

                    # 위와 마찬가지로 확인하던 중 overlap이 2이상 되면 불필요한 연산을 하지 않도록 break를 할 수 있도록 한다.
                    if n == lst[m]:
                        overlap += 1
                    if overlap >= 2:
                        fail += 1
                        break
                if fail >= 1:
                    break

    # 만약 fail 한 번도 나오지 않았다면 result의 값을 1로 바꿔준다.
    if fail == 0:
        result = 1


    print('#{} {}'.format(tc, result))
































    # fail = 0
    # for i in sub_lst:
    #     overlap = 0
    #     for j in range(9):
    #         if i == sub_lst[j]:
    #             overlap += 1
    #         if overlap == 2:
    #             fail += 1
    #
    # for i in range(9):
    #     overlap = 0
    #     for j in range(9):
    #         if arr[j][i] == sub_lst[j]:
    #             overlap += 1
    #         if overlap == 2:
    #             fail += 1
    #
    # for i in range(0, 9, 3):
    #     for j in range(0, 9, 3):
    #         lst = []
    #         for k in range(3):
    #             for l in range(3):
    #                 lst += [arr[i+k][j+l]]
    #
    #
    #         for n in lst:
    #             overlap = 0
    #             for m in range(9):
    #
    #                 if n == lst[m]:
    #                     overlap += 1
    #                 if overlap >= 2:
    #                     fail += 1
    #
    #
    # if fail >= 1:
    #     result = 0
    # else:
    #     result = 1
    # print('#{} {}'.format(tc, result))




# 1208_Flatten 풀이
# 2022-02-10


import sys
sys.stdin = open("input.txt", "r")


# 테스트 케이스의 개수를 입력받는다.(문제에서 10개)
T = 10


# 최대값을 출력하는 함수를 만들어 준다.
def max_max(box_height):

    box_max = 0

    for i in box_height:
        if box_max < i:
            box_max = i

    return box_max


# 최소값을 출력하는 함수를 만들어 준다.
def min_min(box_height2):

    box_min = 100

    for i in box_height2:
        if box_min > i:
            box_min = i

    return box_min


# 테스트 케이스의 수만큼 진행시켜준다.(문제에서는 10이라 주어짐)
for tc in range(1, T+1):

    # 덤프횟수를 입력받는다.
    N = int(input())

    # 상자들의 개수들을 입력받는다.
    boxs = list(map(int, input().split()))

    # 덤프횟수만큼 작동시켜준다.
    for _ in range(N):

        # 최대값을 -1해주기위한 for문
        for i in range(100):
            if max_max(boxs) == boxs[i]:
                boxs[i] -= 1
                break

        # 최소값을 +1해주기위한 for문
        for j in range(100):
            if min_min(boxs) == boxs[j]:
                boxs[j] += 1
                break

    # 형식에 맞게 출력한다.
    print('#{} {}'.format(tc, max_max(boxs)-min_min(boxs)))








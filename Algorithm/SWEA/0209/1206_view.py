# 1206_View 풀이
# 2022-02-09
# s2

import sys
sys.stdin = open("input.txt", "r")

# 테스트 케이스를 얼만큼 받을지 입력한다.(문제는 10)
T = 10

# 주어진 테스트 케이스만큼 출력하기 위한 for문을 만들어 준다.
for tc in range(1, T+1):

    # 입력하고 싶은 빌딩 숫자를 입력한다.
    K = int(input())

    # 빌딩의 숫자를 리스트 형식으로 입력한다.
    building_cnt = list(map(int, input().split()))

    # building_count의 길이를 구한다.
    cnt = 0
    for _ in building_cnt:
        cnt += 1

    # 조망이 확보된 세대 수를 세기 위하여 view_count 변수를 0으로 만들어 준다.
    view_count = 0

    # 앞의 두 자리와 끝의 두 자리는 0의 값을 가지므로 제외 시키고 for문을 구현한다.
    for i in range(2, cnt-2):

        # 왼쪽 2개, 오른쪽 2개 건물의 크기를 담을 리스트를 만들어 준다.
        lst = [building_cnt[i-2], building_cnt[i-1], building_cnt[i+1], building_cnt[i+2]]

        # lst의 값들을 오름차순 정렬해준다.
        for j in range(3):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]

        # 기준 빌딩의 값에서 lst의 가장 큰 값을 뺀 나머지가 양수일 때 그 수가 조망권이 확보된 세대 수이다.
        if (building_cnt[i] - lst[-1]) > 0:
            view_count += building_cnt[i] - lst[-1]

     # 정해진 양식에 맞게 출력한다.
    print('#{} {}'.format(tc, view_count))


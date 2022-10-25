# 1859_백만장자-프로젝트 풀이
# 2022-02-17


# 뒤에서부터 계산하여 앞에 작은 수가 있으면 차이만큼을 누적합에 더해주고
# 큰 수가 있다면 기준값을 변경하여 맨 앞까지 진행하도록 한다.

import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    price = list(map(int, input().split()))

    benefit = 0         # 누적 이익을 받기 위함
    max_price = 0       # 최대값을 정해주는 것

    M = N - 1           # N - 1에서 출발하기 위한 것
    while M >= 0:       # M이 0까지 실행되도록 설계
        if max_price > price[M]:               # 최대값이 현재 값보다 크면 차이만큼을 누적 이익에 더 해준다.
            benefit += max_price - price[M]
            M -= 1                              # 그리고 M을 한 번 줄여준다(길이 줄이기)
        else:
            max_price = price[M]                # 최대값이 같거나 작으면 최대값을 바꿔준다.
            M -= 1

    print('#{} {}'.format(tc, benefit))
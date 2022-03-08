# 4835_구간합 풀이
# 2022-02-10


import sys
sys.stdin = open("sample_input.txt", "r")


# 테스트 케이스의 개수를 입력받는다.
T = int(input())

for tc in range(1, T+1):

    # 정수의 개수 N과 구간의 개수 M을 입력받기 위한 리스트
    K = list(map(int, input().split()))

    # 정수의 개수 N과 구간의 개수 M을 설정
    N = K[0]
    M = K[1]

    # N개 만큼의 숫자들을 입력받는다.
    numbers = list(map(int, input().split()))

    # 기준값의 양쪽을 구간으로 설정하기 위해 M을 2로 나눈 몫을 area로 설정한다.
    area = M // 2

    # 전체값들의 합을 구하기 위한 for문
    total = 0
    for i in numbers:
        total += i

    # min_number에 전체 합을 넣어주고 그것보다 작은 값들을 차례대로 구한다.
    min_number = total
    # max_number에는 가장 작은 값을 넣어준다.
    max_number = 0


    # 구간을 구해야 하기 때문에 0이나 1부터가 아닌 area부터 시작하여 N-area를 범위로 설정한다.
    # 그리고 max와 min 값을 비교하기 위한 sample변수를 만들어 준다.
    for i in range(area, N-area):
        sample = 0

        # 슬라이싱을 이용하여 i를 기준으로 양 구간까지의 합을 구하고 최소값, 최대값을 구해준다.
        for j in numbers[i - area:i + area + 1]:
            sample += j

        if sample > max_number:
            max_number = sample


        if sample < min_number:
            min_number = sample



    print('#{} {}'.format(tc, max_number-min_number))
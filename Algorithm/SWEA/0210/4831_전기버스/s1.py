# 4831_전기버스 풀이
# 2022-02-10


import sys
sys.stdin = open("sample_input.txt", "r")


T = int(input())


def bus_charge(info_numbers, charger):

    # 각각의 정보를 변수에 넣어준다.
    K = int(info_numbers[0])
    N = int(info_numbers[1])
    M = int(info_numbers[2])

    # 충전기의 개수가 (정류장/최대 이동거리)보다 작다면 절대 도달할 수 없기 때문에 return값을 0으로 잡아준다.
    if N // K > M:
        return 0

    # 전 위치를 설정하기 위한 i
    # 정류장을 들린 횟수를 구하기 위한 cnt
    # 가장 최근에 들린 정류장 번호를 설정하기 위한 chargin_station

    i = 0
    cnt = 0
    charging_station = 0

    # N에 도달하기 위한 i의 모험 시작(첫 시작은 0에서 부터)
    while i < N:

        # 리스트 charger의 값들을 하나씩 뽑아본다. = 충전기가 있는 정류장 번호(j)
        for j in charger:

            # 만약 (현재위치 + 최대 이동거리)가 j보다 크다면 charging_station으로 설정하여 들린 것이라 해준다.
            # for문이기 때문에 들릴 수 있는 j값 중 가장 큰 값이 charging_station으로 설정된다.
            if (i + K) >= j:
                charging_station = j

            # 그게 안된다면 break를 해줘 for문을 벗어나게 한다.
            else:
                break

        # 만약 i(전위치) 와 charging_station(현재위치)가 같다면 최대이동거리에서 벗어난 것이기 때문에 0을 리턴한다.
        if i == charging_station:
            return 0

        # 그게 아니라면 i에 charging_station을 대입하며 개수를 +1해준다.
        i = charging_station
        cnt += 1

        # 길이(N)에서 최대거리(K)를 뺀만큼만 가면 되는 것이기 때문에 if문을 넣어 조건을 만족시킨다면 while문을 벗어나도록 만든다.
        if i >= N - K:
            break

    # 개수를 리턴한다.
    return cnt


# 테스트 케이스의 수만큼 돌려준다.
for tc in range(1, T+1):

    # K,N,M 정보가 담긴 리스트
    info_numbers = list(map(int, input().split()))

    #충전기 위치 정보
    charger = list(map(int, input().split()))

    # 결과
    result = bus_charge(info_numbers, charger)
    print("#{} {}".format(tc, result))


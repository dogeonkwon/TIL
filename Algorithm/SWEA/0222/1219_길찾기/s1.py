# 1219_길찾기 풀이
# 2022-02-22


import sys
sys.stdin = open('input.txt', 'r')


def long(lst):
    cnt = 0
    for _ in lst:
        cnt += 1
    return cnt


T = 10

for _ in range(1, T+1):

    tc, cnt = map(int, input().split())         # 테스트케이스 값, 길이의 총 개수(2개가 한 묶음)를 구해준다.
    num = list(map(int, input().split()))
    starts = list()                             # 시작값들의 모음
    ends = list()                               # 도착값들의 모음
    stack = list()                              # 내가 간 경로(pop할 수 있음)
    visited = list()                            # 방문했던 값들
    result = 0                                  # visited에 내가 찾던 값이 있으면 1로 바꿔줌

    for i in range(cnt*2):                      # 2개가 한 묶음이기 때문에 cnt*2를 해준다.
        if i % 2:
            ends.append(num[i])
        else:
            starts.append(num[i])
    first = 0                       # 출발값
    last = 99                       # 목적지

    visited.append(starts[0])           # 시작값을 visited에 추가해줌
    for n in range(long(starts)):       # 시작값들의 길이만큼 반복문을 돌려줌
        if starts[n] == first:          # 출발값과 같은 시작값을 가지고 있는 도착값들을 stack, visited에 추가해줌
            stack.append(ends[n])
            visited.append(ends[n])

    while stack:                        # stack이 없어질 때까지 반복
        now = stack.pop()               # 제일 최근 stack값을 비교
        for m in range(long(starts)):
            if starts[m] == now and ends[m] not in visited:         # 현재값(now)과 시작값이 같으며 그에 대응하는 도착값이 방문한 적이 없다면 추가.
                stack.append(ends[m])
                visited.append(ends[m])
    for k in visited:
        if k == last:
            result = 1

    print('#{} {}'.format(tc, result))
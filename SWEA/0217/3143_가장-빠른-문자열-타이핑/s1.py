# 3143_가장-빠른-문자열-타이핑 풀이
# 2022-02-17

import sys
sys.stdin = open('sample_input.txt', 'r')


# 길이를 구해주는 함수를 선언
def long(s):

    cnt = 0
    for _ in s:
        cnt += 1
    return cnt


T = int(input())

for tc in range(1, T+1):

    t, p = map(str, input().split())

    # 텍스트의 길이를 구해준다
    N = long(t)

    # 패턴의 길이를 구해준다
    M = long(p)

    # 반복문을 이용해 처음부터 끝까지 겹치는 단어가 있을 때마다 cnt를 1씩 올려준다.
    cnt = 0
    for i in range(N):
        if i + M <= N and t[i:i+M] == p:
            cnt += 1

    # result에는 텍스트의 전체길이에서 ((패턴의 길이 - 1) x cnt의 개수)를 빼준다.
    result = N - ((M-1)*cnt)

    print('#{} {}'.format(tc, result))


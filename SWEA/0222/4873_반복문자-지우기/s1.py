# 4873_반복문자-지우기 풀이
# 2022-02-22

import sys
sys.stdin = open('sample_input.txt', 'r')


def long(lst):
    cnt = 0
    for _ in lst:
        cnt += 1
    return cnt


T = int(input())

for tc in range(1, T+1):

    String = list(map(str, input()))        # 문자값을 받는다.
    n = long(String)                        # 문자값의 길이

    while n > 0:                            # 뒤에서부터 시작(수가 줄어들어도 -1씩 비교할 수 있다)
        n -= 1
        if 1 <= n < long(String):           # n값이 최소 1 이상이어야만 앞의 값과 비교할 수 있고, 문자의 길이보다 작아야 인덱스 에러가 안난다.
            if String[n] == String[n-1]:
                String.pop(n)
                String.pop(n-1)
        else:                               # 위의 조건을 만족하지 못한다면 한 번더 -1을 해준다.
            n -= 1

    print('#{} {}'.format(tc, long(String)))
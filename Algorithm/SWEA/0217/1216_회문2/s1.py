# 1216_회문2 풀이
# 2022-02-17

import sys
sys.stdin = open('input.txt', 'r')


def long(lst):

    cnt = 0
    for _ in lst:
        cnt += 1
    return cnt


T = 10
for tc in range(1, T+1):

    num = int(input())

    arr = [list(input()) for _ in range(100)]

    c_arr = list(zip(*arr))      # 행과 열을 같은 식으로 정리하기 위해 zip을 이용한다.

    N = long(arr)              # 행의 길이

    max_palindrome = 1          # 최대_회문

    for k in range(N, 2, -1):
        for i in range(N):
            for j in range(N-k+1):

                r_sub = arr[i]              # 행의 최대회문을 구하기 위한 코드
                r_result = r_sub[j:j+k]

                c_sub = c_arr[i]            # 열의 최대회문을 구하기 위한 코드
                c_result = c_sub[j:j+k]

                if r_result == r_result[::-1] or c_result == c_result[::-1]:     # 만약 둘 중 하나라도 회문이 된다면 (큰 수부터 비교했으니) 최대_회문변수에 k값을 넣어준다.
                    if max_palindrome < k:
                        max_palindrome = k
                        break

    print('#{} {}'.format(num, max_palindrome))

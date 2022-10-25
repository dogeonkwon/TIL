# 4864_문자열-비교 풀이
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

    # 패턴을 입력받음
    p = input()

    # 텍스트를 입력받음
    t = input()

    # 패턴의 길이를 구함
    N = long(p)

    # 텍스트의 길이를 구함
    M = long(t)

    # M-N+1까지 반복문을 돌려주는데, if문을 사용해서 p(패턴)과 t[i부터 i+N까지]가 같으면 result의 값을 바꿔준다.
    # 아니라면 result는 0으로 출력
    for i in range(M-N+1):
        if p == t[i:i+N]:
            result = 1
            break
        result = 0

    print('#{} {}'.format(tc, result))
# 4861_회문 풀이
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

    # N = 글자판의 길이, M = 회문의 길이
    N, M = map(int, input().split())

    # t는 글자판을 2찬원 배열로 받기위함
    t = [list(map(str, input())) for _ in range(N)]

    # 결과값을 저장해줄 result을 선언
    result = ''

    # 가로에서 회문을 탐색하도록 함
    for i in range(N):

        # N-M+1까지만 탐색하여도 전체를 탐색할 수 있다.(회문의 길이를 포함해야 하므로)
        for j in range(N-M+1):

            # 임의의 값을 저장해줄 sub_result 선언
            sub_result = ''

            # j부터 c까지의 글자를 sub_result에 넣어주고 그 값의 정방향과 역방향이 같은지 검사한다.
            # 만약 같다면 result의 값을 바꿔주며 반복문을 종료
            for c in range(j, j+M):
                sub_result += t[i][c]
            if sub_result == sub_result[::-1]:
                result = sub_result
                break


### 변수명 바꿔서 합칠 수 있음!


    # 세로에서 회문을 탐색하도록 함
    # 가로와 동일한 원리
    for k in range(N):
        for l in range(N-M+1):
            sub_result = ''
            for v in range(l, l+M):
                sub_result += t[v][k]
            if sub_result == sub_result[::-1]:
                result = sub_result
                break

    print('#{} {}'.format(tc, result))

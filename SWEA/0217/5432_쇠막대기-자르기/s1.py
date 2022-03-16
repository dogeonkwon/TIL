# 5432_쇠막대기-자르기 풀이
# 2022-02-17

import sys
sys.stdin = open('sample_input.txt', 'r')


T = int(input())

for tc in range(1, T+1):

    t = input()

    compare = 0     # 전의 값이 '('인지 ')'인지 비교하기 위함
    num = 0         # 막대기의 개수(앞에 쌓인)
    result = 0      # 막대기의 총 개수최

    for i in t:
        if i == ')':
            num -= 1        # 앞에 쌓인 막대기의 개수를 하나 빼준다.(막대기가 시작하지 못했으므로)
            if compare:         # 그리고 닫는 괄호이기 때문에 앞에 여는 괄호가 왔었다면 실행되도록 한다.
                result += num       # 레이저로 막대기를 반토막 냈다는 뜻이므로 결과값에 그 만큼을 더 해준다.
                result -= 1     # '('에 추가된 result + 1 은 레이저 였다는 뜻이므로
            compare = 0         # compare의 상태를 변경해준다.
        else:
            num += 1        # 앞에 쌓인 막대기 개수를 하나 늘려준다.(막대기가 시작했으므로)
            result += 1     # 막대기의 총 개수를 하나 늘려준다.
            compare = 1     # compare의 상태를 변경해준다.

    print('#{} {}'.format(tc, result))
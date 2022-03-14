# 1213_String 풀이
# 2022-02-16

import sys
sys.stdin = open('test_input.txt', 'r', encoding='UTF-8')


# string의 길이를 구하기 위한 함수 선언
def long(s):

    cnt = 0
    for _ in s:
        cnt += 1
    return cnt

# 테스트케이스를 10번 줬다.
T = 10


for tc in range(10):

    # 테스트 케이스 번호
    v = int(input())

    # 패턴을 입력받는다.
    p = input()

    # text를 입력받는다.
    t = input()

    # 패턴의 길이를 구한다.
    N = long(p)

    # text의 길이를 구한다.
    M = long(t)

    cnt = 0

    # M-N+1의 길이만큼 for문을 돌리고 슬라이싱을 이용하여 t[i:i+N]과 p과 같을때마다 카운트를 해준다.
    for i in range(M-N+1):
        if p == t[i:i+N]:
            cnt += 1

    print('#{} {}'.format(v, cnt))
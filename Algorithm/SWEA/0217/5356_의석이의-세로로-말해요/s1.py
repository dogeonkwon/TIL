# 5356_의석이의-세로로-말해요 풀이
# 2022-02-17

import sys
sys.stdin = open('sample_input.txt', 'r')


# 원소의 개수를 구해주는 함수
def long(lst):
    cnt = 0
    for _ in lst:
        cnt += 1
    return cnt

T = int(input())

for tc in range(1, T+1):

    # 텍스트를 2차원 배열로 받아준다.
    t = [list(input()) for _ in range(5)]

    # 텍스트 원소의 개수를 구해준다.
    t_length = 0
    for j in range(long(t)):
        t_length += long(t[j])

    # 텍스트에서 하나씩 추출하여 제일 앞에있는 문자를 pop함수로 뽑아내어 result에 넣어준다.
    # 만약 i가 []가 된다면 continue를 활용해 계속 반복문이 실행되도록 한다.
    # 그러다 result의 길이가 t_length와 같아지면 반복문을 종료한다.
    result = ''
    while t_length != long(result):
        for i in t:
            if i != []:
                result += i.pop(0)
            else:
                continue

    print('#{} {}'.format(tc, result))

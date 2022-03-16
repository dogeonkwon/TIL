# 4865_글자수 풀이
# 2022-02-17

import sys
sys.stdin = open('sample_input.txt', 'r')


T = int(input())

for tc in range(1, T+1):

    # 각 패턴을 입력받는다.(글자 하나 하나)
    str1 = input()

    # 텍스트를 입력받는다.
    str2 = input()

    # 중복되는 값이 생길경우 하나씩 카운트해주기 위해 빈 딕셔너리를 만들어준다.
    dic = {}

    # 각 패턴을 하나씩 뽑아내 딕셔너리에 없다면 0의 값을 가지게 하고 넣어준다.
    for i in str1:
        if i not in dic:
            dic[i] = 0

    # 그렇게 생긴 딕셔너리의 키를 뽑아내 텍스트와 비교해준다.
    # 텍스트에 키 값과 같은 문자가 있을 경우 카운트를 1씩 증가시켜준다.
    for k in dic.keys():
        for j in str2:
            if k == j:
                dic[k] += 1

    # result의 값을 0으로 하여 만들어준다.
    # 반복문을 돌려 만들어진 dic의 값들 중 가장 큰 값을 추출해준다.
    result = 0
    for value in dic.values():
        if result < value:
            result = value


    print('#{} {}'.format(tc, result))
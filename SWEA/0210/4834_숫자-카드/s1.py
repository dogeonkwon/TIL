# 4834_숫자-카드 풀이
# 2022-02-10


import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

# 테스트 케이스만큼 돌려준다.
for tc in range(1, T+1):

    # 카드의 개수를 받는다.
    card_count = int(input())
    # 숫자들을 int형태로 list로 받는다.
    numbers = list(map(int, input()))

    # 숫자들이 얼만큼 나왔는지 count하기 위한 빈리스트를 만든다.
    results = [0] * 10

    # 개수들을 카운트 해준다.
    for i in range(10):
        for number in numbers:
            if i == number:
                results[number] += 1

    # 최대 갯수가 몇 개 인지 찾아준다.
    max_cnt = 0
    for result in results:
        if max_cnt < result:
            max_cnt = result

    # 최대 숫자가 무엇인지 찾아준다.
    max_num = 0
    for j in range(10):
        if max_cnt == results[j]:
            max_num = j


    print('#{} {} {}'.format(tc, max_num, max_cnt))

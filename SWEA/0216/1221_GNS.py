# 1221_GNS 풀이
# 2022-02-16


import sys
sys.stdin = open('GNS_test_input.txt', 'r', encoding='UTF-8')


# 원소들의 개수를 구해주는 함수 long을 선언
def long(lst):

    cnt = 0
    for _ in lst:
        cnt += 1
    return cnt


# 테스트 케이스 수를 입력받는다
T = int(input())

for tc in range(1, T+1):

    # A가 문자열, B가 정수형으로 받아야 하기 때문에 둘 다 정수형으로 입력을 받고 B는 바로 밑에서 정수형으로 변환한다.
    A, B = input().split()
    N = int(B)

    # text를 입력받는다.
    text = list(map(str, input().split()))

    # 순서의 기준을 세우기 위한 리스트
    lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    # 결과를 담을 빈 리스트를 만들어 준다.
    result = []

    # text를 lst 순서대로 result에 차곡차곡 쌓아준다.
    for i in lst:
        for j in text:
            if i == j:
                result += [j]

    # M은 result의 원소의 개수이다.
    M = long(result)

    # A를 먼저 출력한 후 반복문을 시작한다.
    print('{}'.format(A))

    # 겹치는 순서대로 정리했기 때문에 그대로 나오면 되지만 마지막 값만 뒤에 빈칸을 안 달고 출력해주기 위해 별도의 if문을 지정한다.
    for k in range(M):
        if k + 1 == M:
            print(result[k])
        else:
            print(result[k], end=' ')
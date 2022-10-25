# 1945_간단한-소인수분해 풀이
# 2022-02-10


import sys
sys.stdin = open("input.txt", "r")


# 테스트 케이스의 개수를 입력받는다.
T = int(input())

for tc in range(1, T+1):

    # 숫자 N을 입력받는다.
    N = int(input())

    # 나눌 소수를 리스트로 정렬해준다. 큰 값들부터 차례대로 나눌 수 있도록 한다.
    prime_number = [11, 7, 5, 3, 2]
    #결과값을 받을 빈 리스트를 만들어준다.
    result = [0] * 5

    # while문을 이용해서 N이 prime_number로 나눴을 때 0이 된다면 나눠진다는 의미이므로 N을 나눈 몫을 N으로 대입시켜준다. 그리고 자리에 맞는 result의 값을 1씩 올려준다. 또한 다음에도 같은 수로 나눠질 수 있으므로 i의 값을 유지
    # 그게 아니라면 i에 +1을 해준다.
    i = 0
    while i < 5:
        if not N % prime_number[i]:
            N //= prime_number[i]
            result[i] += 1
        else:
            i += 1


    # 여러 값들을 순서대로 출력하기 위해 end='' 함수를 사용하며 중간에 띄워쓰기를 유의해야 한다.
    print('#{}'.format(tc), end=' ')

    # result는 큰 값부터로 구성되어 있으므로 역순으로 출력한다.
    for j in result[::-1]:
        print('{}'.format(j), end=' ')

    # 결과와 결과사이 띄우기 위해 만들었다.
    print()
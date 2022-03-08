# 5789_현주의-상자바꾸기 풀이
# 2022-02-10


import sys
sys.stdin = open("sample_input.txt", "r")

# 테스트 케이스의 개수를 입력받는다.
T = int(input())


for tc in range(1, T+1):

    # N(상자의 개수)과 Q(작업을 실행 할 횟수)를 입력받기위한 K
    K = list(map(int, input().split()))

    N = K[0]
    Q = K[1]

    # N의 개수대로 빈 박스를 만들어준다.
    boxs = [0] * N

    # Q번 만큼 횟수를 실행시켜 준다.
    for i in range(1, Q+1):

        # L(첫 번째 범위), R(마지막 범위)를 받기 위한 G
        G = list(map(int, input().split()))

        L = G[0]
        R = G[1]

        # 범위만큼 boxs의 값을 i로 바꿔주기 위한 for문
        for j in range(L, R+1):
            boxs[j-1] = i

    print('#{}'.format(tc), end=' ')

    # 형식에 맞게 출력하기 위한 for문(!!!마지막 end에 ' '이 같이 출력되면서 오류가 나왔다!!!)
    cnt = 0

    for l in boxs:
        if cnt == N-1:
            print('{}'.format(l))
        else:
            print('{}'.format(l), end=' ')
            cnt += 1

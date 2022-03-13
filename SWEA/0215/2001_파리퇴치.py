# 2001_파리퇴치 풀이
# 2022-02-15


import sys
sys.stdin = open('input.txt', 'r')



T = int(input())

for tc in range(1, T+1):

    # 문제에 주어진 형식에 맞게 값들을 받도록 설정해주자
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 값들의 합을 비교하기 위해 변수를 설정
    result = 0

    # 전체 범위를 지나가기 위한 반복문
    for i in range(N):
        for j in range(N):

            # 지나가다 만약 행과 열에 파리채 길이만큼을 뺀 뒤 +1을 했을 때 0이 넘지 않는다면 이제 합을 구해본다
            # if문이 성립할 때마다 매번 total값을 0으로 초기화 시켜 준다.
            if i-M+1 >= 0 and j-M+1 >= 0:
                total = 0

                # k(제일 왼쪽 위 행)와 l(제일 왼쪽 위 열)에서 부터 i, j까지 탐색을 하면서 하나씩 값을 더해준다.
                # ex) k = 0, l = 0, i = 1, j = 1, M = 2일때, total의 결과는 12가 된다.
                # [[1, 2, 3]
                #  [4, 5, 6]        <= arr 예시 형태
                #  [7, 8, 9]]
                for k in range(i-M+1, i+1):
                    for l in range(j-M+1, j+1):
                        total += arr[k][l]

                # for문이 완료되면 total과 result를 비교하여 total이 더 크다면 result를 갱신시켜 준다.
                if total > result:
                    result = total


    print('#{} {}'.format(tc, result))

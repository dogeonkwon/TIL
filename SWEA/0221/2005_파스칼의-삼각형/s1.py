# 2005_파스칼의-삼각형 풀이
# 2022-02-21


import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    arr = [[0]*i for i in range(1, N+1)]    # 파스칼 삼각형모양의 빈 리스트를 만든다.
    arr[0][0] = 1       # 첫 번째 줄은 항상 1.

    for i in range(1, N):           # 첫 번째 줄 생략
        for j in range(i+1):        # 행의 번호만큼 열이 있음
            if j == 0:              # 처음 과 끝은 항상 1
                arr[i][j] = 1
            elif j == i:
                arr[i][j] = 1
            else:                   # 나머지 인덱스는 왼쪽 상단값과 오른쪽 상단 값의 합으로 이루어져있다.
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print('#{}'.format(tc))
    for k in arr:
        print(*k)
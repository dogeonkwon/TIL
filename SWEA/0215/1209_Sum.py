# 1209_Sum 풀이
# 2022-02-15


import sys
sys.stdin = open('input.txt', 'r')


# 리스트 안에 있는 원소의 개수를 구하기 위한 함수
def long(lst):

    cnt = 0
    for _ in lst:
        cnt += 1
    return cnt

# 문제에서 10개의 테스트 케이스를 갖는다고 나와있음.
T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    # 행의합 중 가장 큰값 = 열의합 중 가장 큰값 = 대각선의 합 중 큰 값 = 0 으로 세팅
    result = result2 = result3 = 0

    # 열의 합을 비교하여 제일 큰 값을 result에 넣는다.
    for i in range(long(arr[0])-1):
        total = 0
        total2 = 0
        for k in range(long(arr)):
            total += arr[k][i]
            total2 += arr[k][i+1]

        if total > total2:
            if result < total:
                result = total
        else:
            if result < total2:
                result = total2

    # 행의 합을 비교하여 제일 큰 값을 result2에 넣는다.
    for j in range(long(arr)-1):
        total3 = 0
        total4 = 0
        for l in range(long(arr)):
            total3 += arr[j][l]
            total4 += arr[j+1][l]

        if total3 > total4:
            if result2 < total3:
                result2 = total3
        else:
            if result2 < total4:
                result2 = total4

    # 대각선의 합을 비교하여 제일 큰 값을 result3에 넣는다.
    total5 = total6 = 0
    for m in range(long(arr)):
        total5 += arr[m][m]
        total6 += arr[long(arr)-1-m][long(arr)-1-m]
    if total5 > total6:
        result3 = total5
        total5 = total6 = 0
    else:
        result3 = total6
        total5 = total6 = 0

    # 합들의 차를 구해서 양수라면 제일 큰 값으로 출력
    if result - result2 >= 0 and result - result3 >= 0:
        print('#{} {}'.format(N, result))
    elif result2 - result >= 0 and result2 - result3 >= 0:
        print('#{} {}'.format(N, result2))
    else:
        print('#{} {}'.format(N, result3))



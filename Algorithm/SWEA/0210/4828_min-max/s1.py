# 4828_min-max 풀이
# 2022-02-10


import sys
sys.stdin = open("sample_input.txt", "r")

# test case를 입력받는다.
T = int(input())

for i in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    # 리스트 a를 정렬하여 첫 번째에 제일 작은 값이, 마지막에 제일 큰 값이 나올 수 있도록 만든다.
    # for문을 2개 이용하여 a[j]가 오른쪽에 있는 수 보다 클 경우 그 위치를 바꾸도록 만든다.
    for j in range(N-1):
        for k in range(j+1, N):
            if a[j] > a[k]:
                a[j], a[k] = a[k], a[j]

    print('#{} {}'.format(i, a[-1]-a[0]))
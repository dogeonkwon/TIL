# 델타탐색 풀이
# 2022-02-14

import random

arr = [[i+j for j in range(1, 6)] for i in range(0, 25, 5)]

random.shuffle(arr)

# i(행)과 j(열)이 움질일 범위를 설정해준다.
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N = int(input())

# 값들의 합을 받을 함수를 입력해준다.
total = 0

# for문을 3개 사용한다.
# 첫 번째는 행의 숫자만큼
# 두 번째는 열의 숫자만큼
# 세 번째는 움직일 범위의 숫자만큼
for k in range(N):
    for l in range(N):
        for m in range(4):

            # 움직인 값을 ni, nj에 각각 넣어준다.
            ni = k + di[m]
            nj = l + dj[m]

            # ni, nj가 0보다 작거나 N보다 커진다면 인덱스를 벗어나게 되므로 if문을 사용한다.
            if 0 <= ni < N and 0 <= nj < N:

                # 첫 번째 if문을 통과한 값들과 기준값의 차이를 절대값으로 더해줘야 한다.
                if arr[k][l]-arr[ni][nj] < 0:
                    total -= arr[k][l]-arr[ni][nj]
                else:
                    total += arr[k][l]-arr[ni][nj]

print(total)
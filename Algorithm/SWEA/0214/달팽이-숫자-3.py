# 달팽이-숫자 풀이
# 2022-02-14


# len함수를 대체하기 위해 길이를 구해주는 length함수를 선언
def length(sub_lst):
    cnt = 0
    for _ in sub_lst:
        cnt += 1
    return cnt

# 보기에서 주어진 2차원 리스트를 따라 만들기!(없다면 그냥 행과 열을 보고 빈 2차원 리스트를 만들기!)
arr = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]


# N은 주어진 2차 배열 행의 길이!, M은 2차 배열 열의 길이!
N = length(arr)
M = length(arr[0])

# 일단 보기에서 주어진 배열의 값을 전부 0으로 만들기!
for i in range(N):
    for j in range(M):
        arr[i][j] = 0

# 기준점에서 열과 행을 얼만큼 움직일지 정하기 위한 것!
r = c = 0

# 오른쪽(0), 아래(1), 왼쪽(2), 위(3)로 움직이기 위한 일종의 조이스틱!
control = 0

# control의 값에 따라 행과 열을 움직여줄 리스트!
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 1부터 주어진 배열의 세로 X 가로만큼 숫자를 넣기 위한 for문!
for num in range(1, N * M + 1):

    # arr의 첫 번째 자리에 num값을 넣어주면서 시작!
    arr[r][c] = num

    # dr,dc[control]을 통해 주어진 범위 끝까지 작동할 수 있도록 함!
    r += dr[control]
    c += dc[control]

    # r과 c값이 arr의 인덱스 번호를 뜻하는데 이 값이 0 미만으로 떨어지거나 N(행), M(열)의 길이보다 커지거나 인덱스로 찾은 값이 0이 아닌 다른 수로 채워져 있을 경우 경로를 벗어난 것이므로 if문을 통하여 수정해줌
    if r < 0 or r >= N or c < 0 or c >= M or arr[r][c] != 0:

        # 진행되었던 r과 c 값을 그 전 상태로 돌려놓고
        r -= dr[control]
        c -= dc[control]

        # control값을 + 1 하고 4로 나눈 나머지를 넣어주면 다시 정상적으로 자리를 잡음
        control = (control + 1) % 4

        # 그리고 다시 했던 작업을 반복!
        r += dr[control]
        c += dc[control]


print(arr)

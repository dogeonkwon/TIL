# 달팽이-숫자 풀이
# 2022-02-14



# 함수를 만들어서 풀어 보자!
# 배열, 첫 시작 인덱스(st, st), 열 길이, 시작값(넣을값)
def snail(arr, st, length, num):

    # 마지막 값은 시작 인덱스 + 열의 길이 - 1이 된다. ex) 4
    last = st + length - 1

    # 열의 길이만큼 오른쪽으로 계속 이동하게 하는 반복문
    for k in range(st, last + 1):
        arr[st][k] += num
        num += 1

    # st + 1을 한 뒤 열의 길이만큼 아래로 계속 이동하게 하는 반복문
    for l in range(st + 1, last + 1):
        arr[l][last] = num
        num += 1

    # 왼쪽으로 가기 위해 last - 1에서 st - 1까지 인덱스 값이 줄어들면서 이동하게 하는 반복문
    for n in range(last - 1, st - 1, -1):
        arr[last][n] = num
        num += 1

    # 위로 가기 위해 last - 1에서 st까지 인덱스 값이 줄어들면서 이동하게 하는 반복문
    for m in range(last -1, st, -1):
        arr[m][st] = num
        num += 1

    # 그리고 arr이 아니라 num을 리턴하는 이유는 밑에서 알 수 있지!
    return num

# q는 열과 행의 길이(같다는 전제)
q = 5

# 0이 들어있는 5X5 배열을 만들어준다.
sample = [[0 for _ in range(q)] for _ in range(q)]

# 이 함수는 사각형 테두리 값을 구해주는 함수이기 때문에 3번 동작시켜야 해!(이 부분 개선 필요)
# result에 num값이 입력 되므로 처음 값을 제외하고 시작값은 result를 계속 넣어주면 돼!
# 구조 : result = snail <- 함수 (sample / 0(초기 인덱스 ex) 0, 0을 뜻함 / 5는 배열의 길이 / 1은 처음 넣을 값)
result = snail(sample, 0, 5, 1)

result = snail(sample, 1, 3, result)

result = snail(sample, 2, 1, result)

print(*sample, sep='\n')
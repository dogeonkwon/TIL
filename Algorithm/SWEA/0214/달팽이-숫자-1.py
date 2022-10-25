# 달팽이-숫자 풀이
# 2022-02-14



## 잘못된 코드 ##
# 조건을 잘 못 지정해서 while 문이 끝나지 않는다.
# 앞으로 이런 코드 짜지 않도록 주의하자!

def length(lst):

    cnt = 0
    for _ in lst:
        cnt += 1
    return cnt



N = int(input())

arr = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]

num = 1
st = 0
last = length(arr) - 1
M = length(arr)

for i in range(length(arr)):
    for j in range(length(arr[i])):
        arr[i][j] = 0



while num <= N*N:

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]



    for k in range(1, M):
        if arr[st][st+k] == 0:
            arr[st][st+k] = num
            num += 1
        else:
            continue

    for l in range(1, M):
        if arr[st+l][last] == 0:
            arr[st+l][last] = num
            num += 1
        else:
            continue

    for q in range(1, M):
        if arr[last][last-q] == 0:
            arr[last][last-q] = num
            num += 1
        else:
            continue

    for w in range(1, M):
        if arr[last-w][st] == 0:
            arr[last-w][st] = num
            num += 1
        else:
            continue


print(arr)
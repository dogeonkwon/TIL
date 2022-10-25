import sys

# 조합을 활용 [0, 1], [0, 2], [1, 2]
# 순열은 [0, 1], [1, 0]을 다르게 봄
def tall_sum(n, r, s):
    global stop

    # 가지치기
    if stop or sum(s) > 100:
        return
    elif n == 0:
        if sum(s) == 100:
            stop = 1
            s.sort()
            for j in s:
                print(j)
    # 배열에 담아둔 수를 탐색하면서 새로운 배열인 s에 없거나 s의 최고값보다 큰 값을 추가해준다.
    else:
        for i in range(9):
            if r[i] not in s or i > max(s):
                s.append(r[i])
                # 재귀함수
                tall_sum(n-1, r, s)
                s.pop()


arr = []
stop = 0
for i in range(9):
    arr.append(int(sys.stdin.readline()))

tall_sum(7, arr, [])

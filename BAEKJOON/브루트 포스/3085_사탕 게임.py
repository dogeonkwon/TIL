import sys

input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for _ in range(n)]
res = 1

# 모든 배열을 검색
# 기준점에서 방향을 정하고 같은 문자가 있을 경우에만 카운팅
for i in range(n):
    for j in range(n):
        # 델타탐색 - 어느 방향으로 탐색할 것인지 설정
        for k in (1, 0), (0, 1), (-1, 0), (0, -1):
            y = i
            x = j
            stand = arr[y][x]   # 탐색 시작점
            tmp = 1     # 탐색시작점 카운팅
            stop = 0    # 멈추게 하기 위한 변수

            # 탐색시작!
            # 배열 범위에 포함되고 stop이 2보다 작으면 진행
            while 0 <= y+k[0] < n and 0 <= x+k[1] < n and stop < 2:
                if stand == arr[y + k[0]][x + k[1]]:    # 탐색방향의 문자가 기준점과 같으면 카운팅
                   tmp += 1
                   y += k[0]
                   x += k[1]
                elif stop:      # 이미 한 번 바꿨기 때문에 다시 못 바꾸게 함
                    break
                else:   # 탐색방향과 기준점이 다르다면
                    y += k[0]   # 다음 탐색으로 일단 이동
                    x += k[1]
                    turn = 0    # 90도로 꺽어서 같은 문자가 있을 경우
                    stra = 0    # 같은 방향으로 같은 문자가 있을 경우
                    for v in (1, 0), (0, 1), (-1, 0), (0, -1):  # 다시 델타탐색
                        if 0 <= y + v[0] < n and 0 <= x + v[1] < n:

                            # 90도로 꺽었을 경우
                            if v[0] != k[0] and v[1] != k[1]:
                                if stand == arr[y+v[0]][x+v[1]]:
                                    turn = 1
                            # 같은 방향인 경우
                            elif v[0] == k[0] and v[1] == k[1]:
                                if stand == arr[y + v[0]][x + v[1]]:
                                    stra = 1
                    # 90도로 꺽었을 때만 더 진행될 수 있음
                    if turn:
                        tmp += 1
                        stop += 1
                    elif stra:
                        tmp += 1
                        stop += 3
                    else:
                        stop += 5
            if tmp > res:
                res = tmp
print(res)
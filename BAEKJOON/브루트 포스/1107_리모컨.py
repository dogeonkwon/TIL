import sys

input = sys.stdin.readline

n = str(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
arr = [1] * 10
if m:

    broken = list(map(int, sys.stdin.readline().strip().split()))
    for i in broken:
        arr[i] = 0

up_down = 0
tmp = ''
for i in n:
    s = 20
    plus = 0
    if up_down == 0:
        for j in range(10):
            if arr[j]:
                absolute_number = abs(int(i) - j)
                if s >= absolute_number:
                    s = absolute_number
                    plus = str(j)
        if plus:
            if int(plus) > int(i):
                up_down = 2
            elif int(plus) < int(i):
                up_down = 1

    elif up_down == 1:
        for j in range(9, -1, -1):
            if arr[j]:
                plus = str(j)
                break

    else:
        for j in range(10):
            if arr[j]:
                plus = str(j)
                break
    if plus:
        tmp += plus

res = abs(int(n) - int(tmp)) + len(n)

if abs(int(n)-100) >= res:
    print(res)
else:
    print(abs(int(n)-100))

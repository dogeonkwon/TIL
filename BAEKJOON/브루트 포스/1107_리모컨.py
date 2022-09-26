import sys

input = sys.stdin.readline

n = str(input().strip())
m = int(input().strip())
arr = [1] * 10
if m:
    broken = list(map(int, input().strip().split()))
    for i in broken:
        arr[i] = 0

tmp = ''
for i in n:
    s = 20
    plus = 0
    for j in range(10):
        if arr[j]:
            absolute_number = abs(int(i) - j)
            if s >= absolute_number:
                s = absolute_number
                plus = str(j)
    if plus:
        tmp += plus

res = abs(int(n) - int(tmp)) + len(n)

if abs(int(n)-100) >= res:
    print(res)
else:
    print(abs(int(n)-100))

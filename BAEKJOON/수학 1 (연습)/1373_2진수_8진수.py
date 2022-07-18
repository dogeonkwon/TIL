import sys

two = sys.stdin.readline().strip()[::-1]

ans = ''

for i in range(0, len(two), 3):
    tmp = two[i:i+3]
    if len(tmp) == 2:
        tmp += '0'
    elif len(tmp) == 1:
        tmp += '00'

    res = int(tmp[0]) * 1 + int(tmp[1]) * 2 + int(tmp[2]) * 4
    ans += str(res)

print(ans[::-1])
import sys

e, s, m = map(int, sys.stdin.readline().split())

res = 1
ee, ss, mm = 1, 1, 1

while True:
    if ee == e and ss == s and mm == m:
        print(res)
        break
    else:
        ee += 1
        ss += 1
        mm += 1
        res += 1
        if ee > 15:
            ee -= 15
        if ss > 28:
            ss -= 28
        if mm > 19:
            mm -= 19
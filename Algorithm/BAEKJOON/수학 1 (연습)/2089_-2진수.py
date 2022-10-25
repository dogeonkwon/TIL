import sys

n = int(sys.stdin.readline())
ans = ''

while n != 0:
    if abs(n) % 2:
       ans += '1'
       n = (n // -2) + 1
    else:
        ans += '0'
        n = (n // -2)

if ans == '':
    print(0)
else:
    print(ans[::-1])
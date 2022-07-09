import sys
import math


n, m = map(int, sys.stdin.readline().split())
fac = int(math.factorial(n) / (math.factorial(m) * math.factorial(n-m)))
ans = 0
for i in str(fac)[::-1]:
    if i == '0':
        ans += 1
    else:
        print(ans)
        break
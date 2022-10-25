import sys

n = int(sys.stdin.readline())
total = 1
ans = 0
for i in range(1, n+1):
    total *= i
for j in str(total)[::-1]:
    if j == '0':
        ans += 1
    else:
        break
print(ans)
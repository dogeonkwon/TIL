import sys

n = sys.stdin.readline().strip()

k = len(n)-1
num = 0
s = ((k // 3) + 1)
ans = [0] * s
for i in n:
    if i == '1':
        if k >= 3:
            ans[k//3] += (k % 3) + 1
        else:
            ans[k//3] += 2**k
    k -= 1

res = ''
for j in ans[::-1]:
    res += str(j)
print(res)

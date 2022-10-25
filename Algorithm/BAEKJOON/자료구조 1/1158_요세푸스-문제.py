import sys

n, m = map(int, sys.stdin.readline().split())
m -= 1
k = m

temp = [i for i in range(1, int(n)+1)]
ans = list()
while temp:
    if m < len(temp):
        ans.append(temp[m])
        temp.remove(temp[m])
    else:
        while m >= len(temp):
            m %= len(temp)
        ans.append(temp[m])
        temp.remove(temp[m])
    m += k
print('<', end='')
for j in range(len(ans)):
    if j == len(ans)-1:
        print(f'{ans[j]}>')
    else:
        print(f'{ans[j]},', end=' ')
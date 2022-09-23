import sys

res = [1, 2, 4] + ([0] * 999998)
print('!!!!!')
for i in range(3, 1000001):
    res[i] = res[i-3] + res[i-2] + res[i-1]
    print('도건')
print('##')
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    print('@@@@')
    print(res[n-1] % 1000000009)
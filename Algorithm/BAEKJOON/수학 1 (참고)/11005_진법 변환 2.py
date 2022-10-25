import sys

N, B = map(int, sys.stdin.readline().strip().split())

res = ''

table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N != 0:
    res += table[N % B]
    N //= B
print(res[::-1])
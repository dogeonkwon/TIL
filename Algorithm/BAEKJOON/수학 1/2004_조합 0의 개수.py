import sys


def f_count(s):
    res = 0
    while s != 0:
        s //= 5
        res += s
    return res


def t_count(s):
    res = 0
    while s != 0:
        s //= 2
        res += s
    return res


n, m = map(int, sys.stdin.readline().split())
ans = min(f_count(n) - f_count(m) - f_count(n-m), t_count(n) - t_count(m) - t_count(n-m))
print(ans)
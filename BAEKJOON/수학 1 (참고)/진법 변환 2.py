import sys

N, B = map(int, sys.stdin.readline().strip().split())

res = ''
# 다른 진법들 처럼 나눈 값의 나머지(k)를 res의 뒤에 더해준다.
# 이 때 10 이상의 수들은 알파벳으로 바꿔 준다.
# 런타임 에러 나옴...

while N > B:
    k = N % B
    if k > 9:
        k = chr(k+55)
    res += k
    N //= B
print(res)

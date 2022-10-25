import sys, math

t = int(sys.stdin.readline())
for _ in range(t):
    k = 0
    m, n, x, y = map(int, sys.stdin.readline().split())

    # 규칙은 생각보다 단순
    # x, y가 최소공배수 보다 커지지 않도록
    # x += m, y += n 하면서 조건에 만족하는 숫자가 있는지 확인
    min_num = m*n // math.gcd(m, n)

    ans = 0
    while x <= min_num:
        if not (x - y) % n:     # not (x - y) % n 이라는 조건을 생각하는 것이 어려웠다.
            print(x)
            ans = 1
        x += m
    if not ans:
        print(-1)
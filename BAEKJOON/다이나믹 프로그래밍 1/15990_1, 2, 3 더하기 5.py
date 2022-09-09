import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    # 세 가지 규칙을 생각함
    # 1 2 3 | 4 5 6 | 7 8 9 | 10
    # 1 1 3 | 3 4 8 | 9 13 23 | 27
    if n % 3 == 1:
        m = n // 3
        print(3**m % 1000000009)
    elif n % 3 == 2:
        m = n // 3
        k = 3**m
        print((k + k//2) % 1000000009)
    else:
        m = n // 3
        k = 3**m // 3 // 2
        print((3**m - k) % 1000000009)

import sys

# 유클리드 호제법
def gcd(A, B):
    if not B:
        return A
    return gcd(B, A % B)


n = int(sys.stdin.readline())

for _ in range(n):
    A, B = map(int, sys.stdin.readline().strip().split())
    gcd_result = gcd(A, B)
    result = gcd_result * (A / gcd_result) * (B / gcd_result)
    print(int(result))
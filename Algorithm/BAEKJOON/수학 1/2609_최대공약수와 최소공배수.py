import sys

# 유클리드 호제법
def gcd(A, B):
    if not B:
        return A
    return gcd(B, A % B)


A, B = map(int, sys.stdin.readline().strip().split())
gcd_result = gcd(A, B)  # 최대공약수
lcm = gcd_result*(A/gcd_result)*(B/gcd_result)  # 최소공배수

print(gcd_result)
print(int(lcm))
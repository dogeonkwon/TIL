# 4869_종이붙이기 풀이
# 2022-02-22


import sys
sys.stdin = open('sample_input.txt', 'r')


def function(n):        # 10일 경우 1, 20일 경우 3, 30일 경우 5, 40은 11, 50은 21
    if n == 10:         # 문제의 규칙은 a = a(n-10) + (2*a(n-20))과 같으므로 거기에 맞는 함수를 만든다.
        return 1
    elif n == 20:
        return 3
    else:
        return function(n-10) + (2*function(n-20))


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = function(N)

    print('#{} {}'.format(tc, result))
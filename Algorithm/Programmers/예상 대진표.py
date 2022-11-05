def solution(n, a, b):
    answer = 0
    m = small = big = 0
    start = 1

    if a > b:
        small = b
        big = a
    else:
        small = a
        big = b

    while n > 1:
        n //= 2
        m += 1

    while m > 1:
        m -= 1
        if start <= small < start + 2 ** m and start + 2 ** m <= big < start + 2 ** (m + 1):
            return m + 1
        if start + 2 ** m <= small:
            start = start + 2 ** m

    return m
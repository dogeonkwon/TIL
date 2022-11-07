def solution(n):
    if n < 3:
        return n
    else:
        arr = [0] * (n + 1)
        arr[1] = 1
        arr[2] = 2

        for i in range(3, n + 1):
            arr[i] = (arr[i - 1] + arr[i - 2]) % 1234567

        return arr[n]
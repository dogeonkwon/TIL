def solution(phone_book):
    answer = True
    n = len(phone_book)

    arr = sorted(phone_book)
    for i in range(n - 1):
        m = len(arr[i])
        if arr[i] == arr[i + 1][0:m]:
            answer = False
            break


    return answer
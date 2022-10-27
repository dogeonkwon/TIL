def solution(plain):
    n = len(plain)
    answer = 0

    if plain == plain[::-1]:
        return n

    for i in range(n-1):
        sub = plain + plain[0:i+1][::-1]
        if sub == sub[::-1]:
            answer = len(sub)
            break

    return answer


print(solution('bbb'))
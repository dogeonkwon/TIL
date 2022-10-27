def solution(plain):
    n = len(plain)
    answer = 0

    # 주어진 문자열에서 팰린드롬이 되는 문자열의 최대 길이를 구하고(왼쪽에서 시작해서 오른쪽으로 시작점 이동)
    # 팰린드롬을 구하였다면 남은 왼쪽 문자열을 더해준다.
    for i in range(n):
        if plain[i:] == plain[i:][::-1]:
            answer = n + i
            break

    return answer

print(solution('abab'))
print(solution('abcde'))
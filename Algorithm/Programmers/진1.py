def solution(waiting):

    # dict.fromkeys()를 활용해 기존 리스트의 순서를 유지하며 중복을 제거합니다.
    # 이후 list로 다시 변경
    answer = list(dict.fromkeys(waiting))

    return answer

print(solution([1, 5, 8, 2, 10, 5, 4, 6, 4, 8]))
print(solution([5, 4, 4, 3, 5]))
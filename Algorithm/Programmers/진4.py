def solution(sticker):

    n = len(sticker)

    # dp형식으로, 가장 큰 값을 저장하는 방법으로 진행하기 위한 배열
    arr = [0] * n

    # 처음 스티커를 사용한다는 것으로 가정
    arr[0] = sticker[0]

    # 그 다음부터 기존의 값들과 비교하며 진행
    for i in range(1, n):
        # 현재 위치(i)의 스티커를 사용하려면 양쪽을 못 쓰게 되므로 => arr[i-2] + sticker[i]
        # 이 전까지의 최대값 => arr[i-1]
        # 둘 중 큰 값으로 arr[i] 저장
        arr[i] = max(arr[i-2]+sticker[i], arr[i-1])

    answer = arr[-1]
    return answer


print(solution([12, 80, 14, 22, 100]))
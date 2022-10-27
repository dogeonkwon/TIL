import collections


# 문제에 나와 있는 암호화를 역순으로 진행
def solution(encrypted_text, key, rotation):
    answer = ''

    # tmp라는 변수에 deque의 rotate를 활용하여 rotation의 크기만큼 회전시켜 줍니다.
    tmp = collections.deque(encrypted_text)
    tmp.rotate(-rotation)

    # 회전된 tmp를 res에 리스트로 저장
    res = ''.join(list(tmp))

    # key에 대응하는 숫자만큼 앞쪽으로 이동
    # 'a' ~ 'z'는 1~26까지의 숫자
    for i in range(len(res)):
        # ord를 활용하여 대응하는 숫자만큼 앞쪽으로 이동시킨 값을 alpha_num에 저장
        alpha_num = ord(res[i]) - 1 - abs(ord('a') - ord(key[i]))

        # ord('a')를 기존으로 대소를 비교 후 chr를 활용하여 다시 문자열로 answer에 저장
        if alpha_num < ord('a'):
            answer += chr(ord('z') - ord('a') + alpha_num + 1)
        else:
            answer += chr(alpha_num)

    return answer

print(solution('qyyigoptvfb', 'abcdefghijk', 3))
# 정수를 문자열로 변환
# 2022-02-16


# 숫자를 문자열로 바꾸는 string함수를 만들어 준다.
def string(s):

    # 빈리스트를 만들어주고 결과 값으 여기에 넣는다.
    result = ''

    # 받은 정수가 0 이하가 될때까지 반복한다.
    while s > 0:

        # 문자'0'을 ord로 숫자로 만들어 준뒤 s의 일의 자리를 더 해준다. 그리고 chr로 다시 문자열로 바꾼 뒤 result에 결과갑을 넣어주는 연산을 반복한다.
        result = chr(ord('0') + (s % 10)) + result

        # 위 연산이 끝나면 s를 10으로 나눈 몫을 s에 대입해준다.
        s //= 10

    return result

# ex)
print(string(20))

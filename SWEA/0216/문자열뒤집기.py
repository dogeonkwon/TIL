# 문자열뒤집기 풀이
# 2022-02-16

# 문자열을 거꾸로 뒤집어서 출력하는 함수를 만든다.
def rvs(s):

    result = ''
    for i in s:
        result = i + result
    return result

s = 'Reverse this strings'

print(rvs(s))

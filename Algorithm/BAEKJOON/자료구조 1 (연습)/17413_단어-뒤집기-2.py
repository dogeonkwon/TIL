import sys

s = sys.stdin.readline().strip()
n = m = 0   # n : 문자열 시작 인덱스 / m : 문자열 끝 인덱스
ans = ''    # 정답 문자열

while n < len(s):       # n이 s의 길이보다 크거나 같아진다면 중단
    if s[n] == '<':     # s[n]이 '<'를 일 때
        m = s[n::].find('>') + n + 1    # '>'까지를 ans에 그대로 넣어줌
        ans += s[n:m]
        n += (m-n)
    elif s[n] != ' ':       # s[n]이 '<'와 ' '이 아닐 때
        a = b = c = 9999999         # find함수의 경우 없다면 -1이 나온다. 최소값을 찾아야 하므로 값이 없다면 9999999로 유지
        if s[n::].find(' ') > 0:
            a = s[n::].find(' ')
        if s[n::].find('<') > 0:
            b = s[n::].find('<')
        if len(s)-n >= 0:
            c = len(s)-n
        m = n + min(a, b, c)        # 최소 인덱스까지 뒤집어서 ans에 삽입
        if min(a, b, c) == a:
            ans += ''.join(reversed(s[n:m]))
            ans += ' '
            n += (m-n+1)
        else:
            ans += ''.join(reversed(s[n:m]))
            n += (m-n)
    else:       # s[n]이 ' '(공백)일 경우 n에 1을 더해줌
        n += 1
print(ans)

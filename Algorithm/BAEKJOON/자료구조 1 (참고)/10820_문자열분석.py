import sys

# 소문자, 대문자, 숫자, 공백의 개수
while True:
    line = sys.stdin.readline().rstrip('\n')
    if not line:
        break
    ans = [0] * 4
    for i in line:
        if 97 <= ord(i) <= 122:
            ans[0] += 1
        elif 65 <= ord(i) <= 90:
            ans[1] += 1
        elif 48 <= ord(i) <= 57:
            ans[2] += 1
        else:
            ans[3] += 1
    print(*ans)
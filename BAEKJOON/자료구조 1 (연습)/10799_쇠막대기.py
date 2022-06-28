import sys

bracket = sys.stdin.readline()
n = len(bracket)
m = ans = 0
for i in range(n):      # 괄호를 검사하여 (( 이 연속으로 나오면 ans += 1, m에 1씩 추가
    if bracket[i] == '(':
        if bracket[i+1] == '(':
            ans += 1
            m += 1
        else:           # )이 나온다면 ans += m
            ans += m
    else:
        if bracket[i-1] == ')':     # )) 이 나왔다면 m -= 1
            m -= 1
print(ans)
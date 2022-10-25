# 괄호-검사 풀이
# 2022-02-21


stack = input()
arr = []
cnt = 0

for i in stack:             # 입력받은 값들을 하나씩 검사한다.
    if i == '(':            # 값이 '('라면 arr에 추가하고 cnt에 1을 더해준다.
        arr.append('(')
        cnt += 1
    elif i == ')':          # 값이 ')'라면 arr에 값을 pop하고 cnt에 1을 빼준다.
        arr.pop(-1)
        cnt -= 1

if arr == [] and cnt == 0:      # arr이 빈 값이고 cnt가 0이라면 True, 아니라면 False
    print('True')
else:
    print('False')

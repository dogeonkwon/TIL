# 후위표기법 풀이
# 22-02-23


# <연습문제1>   # 2 + 3 * 4 / 5
temp = list(map(str, input().split()))
stack = list()          # 연산자를 따로 모아줄 곳
visited = list()        # 피연산자를 모아줄 곳
top = 0
operation = ['+', '-', '*', '/']        # 연산자인지 아닌지 검사하기 위함

for i in temp:
    if i in operation:              # 연산자라면 stack에 저장
        stack.append(i)
    else:                           # 피연산자라면 visited에 저장
        visited.append(i)

while stack:                        # stack이 빈 값이 될때까지 visited에 하나씩 추가
    visited.append(stack.pop())

print(*visited)
# 2 3 4 5 / * +
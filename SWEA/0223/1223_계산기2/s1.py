# 1223_계산기2 풀이
# 2022-02-23


import sys
sys.stdin = open('input.txt', 'r')


def icp(s):                 # 들어가는 연산의 값을 측정(coming)
    dic = {'+':1, '*':2}
    return dic[s]

def isp(s):                 # 들어있는 연산의 값을 측정(stack)
    dic = {'+':1, '*':2}
    return dic[s]


T = 10
for tc in range(1, T+1):

    N = int(input())
    temp = str(input())
    stack = list()          # 임시로 연산을 담아둘 리스트
    visited = list()        # 피연산자를 담고 뒤에 연산을 담아줄 리스트
    result = list()         # 최종 결과를 저장해 줄 리스트

    for i in temp:
        if i == '+' or i == '*':            # i가 연산이라면
            if stack == []:                 # stack에 아무것도 없다면 바로 넣어줌
                stack.append(i)
            elif icp(i) > isp(stack[-1]):       # 연산이 이미 있다면 값을 비교해서 크다면 넣어줌
                stack.append(i)
            else:
                while stack != []:                  # 그렇지 않다면 stack이 빈 값이 되거나 연산값보다 작은 연산값을 가진 연산이 나올때까지 스택을 pop하고 visited 에 추가해
                    if icp(i) <= isp(stack[-1]):
                        visited.append(stack.pop())
                    else:
                        break
                stack.append(i)                 # 그리고 비교의 기준이었던 연산을 스택 마지막에 추가해줌

        else:                       # 피연산자라면 바로 visited에 추가
            visited.append(i)

    while stack != []:                  # 스택에 있는 모든 값을 visited 뒤에 추가
        visited.append(stack.pop())

    for j in visited:
        if j == '+':                    # j가 '+'라면 result의 앞의 값과 앞앞 값을 더해줌
            n = int(result.pop())
            m = int(result.pop())
            result.append(n+m)
        elif j == '*':                  # j가 '+'라면 result의 앞의 값과 앞앞 값을 곱해줌
            n = int(result.pop())
            m = int(result.pop())
            result.append(n*m)
        else:                           # 피연산자라면 result에 더해줌
            result.append(j)

    print('#{} {}'.format(tc, *result))

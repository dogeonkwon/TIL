
# <교재에 나와있는 계산기 만들기 해본것>    # ( 6 + 5 * ( 2 - 8 ) / 2 )

def icp(s):
    dic = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
    return dic[s]


def isp(v):
    dic = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    return dic[v]


temp = list(map(str, input().split()))

stack = list()
visited = list()
top = 0
operation = ['(', '+', '-', '*', '/']


while top < len(temp):

    if temp[top] in operation:
        if stack == [] or stack[-1] not in operation:
            stack.append(temp[top])
        elif icp(temp[top]) > isp(stack[-1]):
            stack.append(temp[top])
        else:
            while icp(temp[top]) <= isp(stack[-1]):
                visited.append(stack.pop())
            stack.append(temp[top])

    elif temp[top] == ')':
        while stack[-1] != '(':
            visited.append(stack.pop())
        stack.pop()

    else:
        visited.append(temp[top])

    top += 1

print(*visited)
# 6 5 2 8 - * 2 / +
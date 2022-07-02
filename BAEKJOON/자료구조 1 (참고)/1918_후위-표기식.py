import sys

string = sys.stdin.readline().strip()

stack = list()
ans = list()
operation_in = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 3, ')' : 3}
operation_out = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0}

for i in string:
    if i in operation_in:
        if i == ')':
            while stack[-1] != '(':
                ans.append(stack.pop())
            stack.pop()
        elif stack:
            while stack and operation_out[stack[-1]] >= operation_in[i]:
                ans.append(stack.pop())
            stack.append(i)
        else:
            stack.append(i)
    else:
        ans.append(i)
while stack:
    ans.append(stack.pop())
for j in ans:
    print(j, end='')
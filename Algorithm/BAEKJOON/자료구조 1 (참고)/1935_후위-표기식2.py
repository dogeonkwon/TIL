import sys

n = int(sys.stdin.readline())
string = sys.stdin.readline().strip()

num = dict()
for i in range(65, 65+n):
    num[chr(i)] = int(sys.stdin.readline())

stack = list()
for j in string:
    if j in ['+', '-', '*', '/']:
        right = stack.pop()
        left = stack.pop()
        if j == '+':
            stack.append(left + right)
        elif j == '-':
            stack.append(left - right)
        elif j == '*':
            stack.append(left * right)
        elif j == '/':
            stack.append(left / right)
    else:
        stack.append(num[j])

print(f'{stack[0]:.2f}')
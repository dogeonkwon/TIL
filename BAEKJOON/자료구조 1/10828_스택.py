import sys  # sys.stdin.readline()을 쓰기 위한 import

n = int(input())

stack = []
for _ in range(n):
    sub = list(map(str, sys.stdin.readline().split()))  # input()이 아니라 sys.stdin.readline()을 해야 시간초과 오류가 안나고 빨리 받아올 수 있음

    if sub[0] == 'push':
        stack.append(int(sub[1]))
    elif sub[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif sub[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif sub[0] == 'size':
        print(len(stack))
    else:
        if not stack:
            print(1)
        else:
            print(0)
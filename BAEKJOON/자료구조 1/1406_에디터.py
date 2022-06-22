import sys

# 커서를 인덱스 번호로 인식하여 더하고 빼주기를 한다면 시간초과!

text = list(sys.stdin.readline().strip())   # 스택을 2개 만들어 커서의 왼쪽 오른쪽으로 분류한다.
temp = list()

# 커서를 이동하는 연산, 값을 추가하거나 삭제하는 연산 모두 append와 pop을 통해 할 수 있어 O(1) 시간의 연산을 보장
for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())

    if command[0] == 'L':
        if text:
            temp.append(text.pop())
    elif command[0] == 'D':
        if temp:
            text.append(temp.pop())
    elif command[0] == 'B':
        if text:
            text.pop()
    elif command[0] == 'P':
        text.append(command[1])

text.extend(reversed(temp))     # 커서의 오른쪽에 있는 스택들을 뒤집어서 원래 스택과 합쳐준다.
print(''.join(text))
# 4866_괄호검사 풀이
# 2022-02-22


import sys
sys.stdin = open('sample_input.txt', 'r')


def push(item, size):       # push 함수 구현(문제에 맞춰 수정)
    global top
    top += 1
    if top >= size:
        return
    else:
        stack[top] = item


def pop():                  # pop 함수 구현(문제에 맞춰 수정)
    global top
    if top <= -1:
        print('underflow')
        return
    else:
        top -= 1
        stack[top+1] = 0


def long(s):                # 원소의 개수 구하는 함수 구현
    cnt = 0
    for _ in s:
        cnt+=1
    return cnt


T = int(input())

for tc in range(1, T+1):

    arr = input()
    size = long(arr)                # arr의 길이를 저장
    stack = [0]*size                # 길이만큼 빈 리스트를 만들어줌
    top = -1                        # push할 경우 +1을 해주면서 저장하므로 top은 -1에서 시작한다.
    cnt = 0

    for i in arr:
        if i == '(':                # i가 '('일 경우 push
            push('(', size)
        elif i == ')':              # i가 ')'일 경우 전의 값이 '('라면 pop, 아니라면 그대로 저장
            if stack[top] == '(':
                pop()
            else:
                push(')', size)
        elif i == '{':              # i가 '{'일 경우 push
            push('{', size)
        elif i == '}':              # i가 '}'일 경우 전의 값이 '{'라면 pop, 아니라면 그대로 저장
            if stack[top] == '{':
                pop()
            else:
                push('}', size)
        else:
            continue

    if stack[0] == 0:               # 짝이 제대로 맞춰졌다면 stack의 첫 번째 값은 0이 된다.
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))

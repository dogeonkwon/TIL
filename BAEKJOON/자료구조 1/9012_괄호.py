import sys


n = int(sys.stdin.readline())
for _ in range(n):
    balance = 0
    bracket = input()       # sys.stdin.readline()의 경우 괄호 맨마지막을 문자열로 인식하지 못함, 따라서 input() 사용
    if bracket.strip()[-1] == '(' or bracket[0] == ')':
        print('NO')
        continue
    for i in range(len(bracket)):
        if bracket[i] == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            print('NO')
            break
    if balance == 0:
        print('YES')
    elif balance > 0:
        print('NO')
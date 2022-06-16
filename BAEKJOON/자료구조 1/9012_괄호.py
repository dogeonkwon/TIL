import sys


n = int(sys.stdin.readline())
for _ in range(n):
    balance = 0
    bracket = sys.stdin.readline()
    
    if bracket[-1] == '(' or bracket[0] == ')':
        print('NO')
        break
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
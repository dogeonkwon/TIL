import sys
import collections

# from collections import deque 은 안되고

# import collections
# collections.deque 이런식으로는 사용 가능

dq = collections.deque()

n = int(sys.stdin.readline())
for _ in range(n):
    command = list(sys.stdin.readline().split())

    if command[0] == 'push_front':
        dq.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        dq.append(int(command[1]))
    elif command[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)
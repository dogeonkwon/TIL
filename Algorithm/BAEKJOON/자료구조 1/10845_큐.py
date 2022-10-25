import sys
import collections

# from collections import deque 은 안되고

# import collections
# collections.deque 이런식으로는 사용 가능

queue = collections.deque()

n = int(sys.stdin.readline())
for _ in range(n):
    command = list(sys.stdin.readline().split())

    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
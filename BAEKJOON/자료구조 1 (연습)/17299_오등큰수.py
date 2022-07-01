import sys
# collections.Counter 를 이용해 풀이도 가능

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# n이 1일 때
if n == 1:
    print(-1)

# n이 2일 때
elif n == 2:
    print(-1, end=' ')
    print(-1)

# n이 3이상일 때
else:
    tmp = [0] * 1000001     # 1000001 대신 max(arr)을 사용하면 틀림
    for j in arr:           # count 함수를 사용하면 시간초과
        tmp[j] += 1

    stack = list()
    ans = [-1] * n
    for i in range(n-1):
        if tmp[arr[i]] >= tmp[arr[i+1]]:
            stack.append([i, arr[i]])
        else:
            ans[i] = arr[i+1]
            while stack:
                if tmp[stack[-1][1]] < tmp[arr[i+1]]:
                    k = stack.pop()
                    ans[k[0]] = arr[i+1]
                else:
                    break
    print(*ans)
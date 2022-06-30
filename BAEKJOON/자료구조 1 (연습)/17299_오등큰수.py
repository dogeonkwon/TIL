import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

# n이 1일 때
if n == 1:
    print(-1)

# n이 2일 때
if n == 2:
    print(-1, end=' ')
    print(-1)

# n이 3이상일 때
# 비교할 수와 다음 수의 값이 같거나 작다면 스택에 담아준다.
# 비교할 수와 다음 수의 값을 count로 알아내 다음 수가 더 크다면 스택에 쌓아 두었던 전의 값들의 인덱스에 맞게 ans를 바꿔줌

else:
    stack = list()
    ans = [-1] * n
    tmp = [0] * (max(lst)+1)
    for i in range(n-1):
        if not tmp[lst[i]]:
            tmp[lst[i]] = lst.count(lst[i])
        if not tmp[lst[i+1]]:
            tmp[lst[i+1]] = lst.count(lst[i+1])
        if tmp[lst[i]] >= tmp[lst[i+1]]:
            stack.append([i, lst[i]])
        else:
            ans[i] = lst[i+1]
            while stack:
                if tmp[stack[-1][1]] < tmp[lst[i+1]]:
                    k = stack.pop()
                    ans[k[0]] = lst[i+1]
                else:
                    break
    print(*ans)
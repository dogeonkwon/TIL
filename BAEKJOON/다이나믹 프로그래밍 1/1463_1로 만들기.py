import sys

N = int(sys.stdin.readline())

# N만큼의 배열을 만들어줌
arr = [0] * (N+1)

for i in range(2, N+1):

    arr[i] = arr[i-1] + 1    # 1을 뺄 수 있는 조건이 있으므로 1을 하나씩 더하며 올라감

    if not i % 3 and arr[i] > arr[i//3]:    # X가 3으로 나누어 떨어지고, i가 i//3의 값보다 크다면
        arr[i] = arr[i//3] + 1        # 작은 값으로 바꿔줌

    if not i % 2 and arr[i] > arr[i//2]:
        arr[i] = arr[i//2] + 1

print(arr[N])
# 1234_비밀번호 풀이
# 2022-02-22


import sys
sys.stdin = open('input.txt', 'r')


def long(lst):
    cnt = 0
    for _ in lst:
        cnt += 1
    return cnt


T = 10

for tc in range(1, T+1):

    N, num = map(str, input().split())
    stack = [10]                        # 처음 값을 비교해야 하기 때문에 0~9까지의 범위에 안들어가는 10을 임의로 추가한다.
    i = 0
    num = list(num)                     # num을 리스트형으로 변환시켜준다.(pop을 쓰기위해)

    while i < long(num):
        if stack[-1] == num[i]:         # stack에 마지막으로 저장한 값이 num[i]값과 같다면
            num.pop(i)                  # 현재 i값과 그 전의 값을 pop으로 제거하며 stack의 마지막 값도 제거한다.
            num.pop(i-1)                # 그리고 숫자들이 앞으로 빈칸만큼 땡겨오기 때문에 i에 -1을 해준다.
            stack.pop(-1)
            i -= 1
        else:
            stack += num[i]             # 그게 아니라면 stack에 num[i]값을 추가하고 i에 +1을 해준다.
            i += 1

    print('#{}'.format(tc), end=' ')
    for j in num:
        print(j, end='')
    print()
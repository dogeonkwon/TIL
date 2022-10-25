import sys

# 스택으로 푸는 문제
# 값들을 스택에 넣은 후 그 다음 값 중 더 큰값이 있다면 스택에 있는 값과 비교하여 큰 값이 나올 때 까지 pop시켜줌
# 차례대로 출력하면 좋겠지만 인덱스 번호에 맞게 풀이
# Unpacking 하기 위해 *ans 를 활용

n = int(sys.stdin.readline())
NGE = list(map(int, sys.stdin.readline().split()))

# n이 1일경우와 2일 경우는 수동으로 작성
if n == 1:
    print(-1)
elif n == 2:
    if NGE[0] < NGE[1]:
        print(NGE[1], end=' ')
        print(-1)
    else:
        print(-1, end=' ')
        print(-1)
else:   # n이 3이상일 경우
    ans = [-1] * n  # 답을 적어줄 ans
    if NGE[0] < NGE[1]:     # NGE의 첫 번째(인덱스 0) 값이 그 다음 값보다 작다면 일단 ans[0]을 수정
        ans[0] = NGE[1]
        tmp = list()
    else:                   # 아니라면 tmp에 첫번째 자리의 인덱스 번호와 값을 추가
        tmp = list([[0, NGE[0]]])
    for i in range(1, n-1):     # 두 번째(인덱스 1) 값부터 다음값과 비교해서 작다면 tmp에 있는 값들과 비교하여 ans값을 변경해줌
        tmp.append([i, NGE[i]])
        if NGE[i] < NGE[i+1]:
            while tmp:
                if tmp[-1][1] < NGE[i+1]:
                    m = tmp.pop()
                    ans[m[0]] = NGE[i+1]
                else:
                    break
    print(*ans)
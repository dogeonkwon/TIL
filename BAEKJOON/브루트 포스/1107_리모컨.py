import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
break_num = list(map(int, sys.stdin.readline().split()))

# +, -만 했을 때
res = abs(100-n)

# 500,000까지 범위인데 1,000,001까지 한 이유는
# 999,999까지도 고려해야 하기 때문 (여기서 하나씩 내려가는게 더 빠를 수 있음)
for i in range(1000001):
    num = str(i)
    # 각 자리 숫자가 고장난 번호에 포함되지 않는다면 더 작은 더 작은지 비교
    for j in range(len(num)):
        if int(num[j]) in break_num:
            break
        elif j == len(num) - 1:
            res = min(res, abs(i - n) + len(num))
print(res)
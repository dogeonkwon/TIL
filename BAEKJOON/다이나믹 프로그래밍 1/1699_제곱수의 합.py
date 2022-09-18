import sys

def dp(num, cnt, s, ans):
    global res

    if cnt == 1:
        if n == s:
            res = ans
    else:
        for k in range(int(num**0.5), 0, -1):
            if res:
                break
            dp(num-(k**2), cnt-1, s+(k**2), ans)


n = int(sys.stdin.readline())
res = 0

if n == int(n**0.5) ** 2:
    res = 1
else:
    for i in range(2, n):
        if res:
            break
        for j in range(int(n**0.5), 0, -1):
            if res:
                break
            else:
                m = j**2
                dp(n-m, i, m, i)

print(res)






# import sys
#
# n = int(sys.stdin.readline())
# res = 0
#
# while n >= 1:
#     print('##', n**0.5)
#     print(int(n**0.5)**2)
#     n -= int(n**0.5)**2
#     res += 1
#
# print(res)
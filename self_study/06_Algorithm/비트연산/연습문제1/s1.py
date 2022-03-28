'''
2
00000010001101
0000000111100000011000000111100110000110000111100111100111111001100111
'''

# import sys
# sys.stdin = open('input.txt', 'r')

## 기본풀이
# T = int(input())
# for tc in range(1, T+1):
#     arr = input()
#
#     # 7개씩 끊어서 계산 하려면
#     length = len(arr) // 7
#     for i in range(length):
#         n = 0
#         for j in range(i*7, i*7+7):
#             # print(j)
#             n = n * 2 + int(arr[j])
#         print(n, end=' ')
#     print()


# 슬라이싱
T = int(input())
for tc in range(1, T+1):
    arr = input()
    part = list()
    for i in range(0, len(arr), 7):
        part.append(arr[i:i+7])
    print(part)
    for i in part:
        print(int(i, 2), end= ' ')
    print()
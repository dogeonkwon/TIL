# 고지식한-패턴검색 풀이
# 2022-02-16


# string의 길이를 구하기 위한 함수 선언
def long(s):

    cnt = 0
    for _ in s:
        cnt += 1
    return cnt


# 전체 텍스트
t = 'dogun is cool'

# 찾을 패턴
p = 'cool'

# 전체 텍스트의 길이
N = long(t)

# 찾을 패턴의 길이
M = long(p)


# 고지식한 패턴 함수 선언
def BruteForce(p, t):
    i = 0   # t의 인덱스
    j = 0   # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M: return i - M     # 검색 성공
    else: return -1     # 검색 실패


print(BruteForce(p, t))
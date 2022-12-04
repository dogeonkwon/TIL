def prime(s):
    ans = True
    if s < 2:
        ans = False
    else:
        for i in range(2, int(s ** 0.5) + 1):
            if not s % i:
                ans = False
    return ans


def solution(n, k):
    answer = 0

    #     # 소수 리스트 만들기
    #     prime_lst = [True] * 1000001
    #     prime_lst[0] = prime_lst[1] = False

    #     for i in range(2, int(1000001 ** 0.5) + 1):
    #         if prime_lst[i] == True:
    #             for j in range(i*i, 1000001, i):
    #                 prime_lst[j] = False

    # 10진수 -> n진수로 변환
    transfer = ''

    while n > 0:
        n, mod = divmod(n, k)
        transfer += str(mod)

    # 변환한 것에서 소수가 몇 개인지 구하기
    res = transfer[::-1]
    m = len(res)
    tmp = ''

    for i in range(m):
        if res[i] == '0':
            if tmp != '' and prime(int(tmp)):
                answer += 1
            tmp = ''
        else:
            tmp += res[i]

    if tmp != '' and prime(int(tmp)):
        answer += 1

    return answer



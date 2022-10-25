def solution(s):
    #     min_num = 9999999999999999999
    #     max_num = -99999999999999999999
    #     tmp = ''

    #     for i in s:
    #         if i == ' ':
    #             if min_num > int(tmp):
    #                 min_num = int(tmp)
    #             if max_num < int(tmp):
    #                 max_num = int(tmp)
    #             tmp = ''
    #         else:
    #             tmp += i
    #     if min_num > int(tmp):
    #         min_num = int(tmp)
    #     if max_num < int(tmp):
    #         max_num = int(tmp)

    #     answer = str(min_num) + ' ' + str(max_num)

    lst = list(map(int, s.split()))
    answer = str(min(lst)) + ' ' + str(max(lst))

    return answer
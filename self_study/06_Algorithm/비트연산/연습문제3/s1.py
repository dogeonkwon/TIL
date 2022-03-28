'''
2
1
0DEC
0269FAC9A0
'''

# 내가 가진 문자열 bit로부터 비교대상인 password를 어디에? 담아서 어떻게? 대조 할 것인가
password = {
    '001101' : 0,
    '010011' : 1,
    '111011' : 2,
    '110001' : 3,
    '100011' : 4,
    '110111' : 5,
    '001011' : 6,
    '111101' : 7,
    '011001' : 8,
    '101111' : 9
}

T = int(input())
for tc in range(1, T+1):
    arr = input()
    # print(arr)
    bit = ''
    for i in range(len(arr)):
        tmp = int(arr[i], 16)
        tmp = bin(tmp).replace('0b', '')
        while len(tmp) != 4:
            tmp = '0' + tmp
        bit += tmp

    # 뒤에서 1 찾기
    for i in range(len(bit)-1, -1, -1):
        if bit[i] == '1':
            point = i
            break

    # 최종 출력 값
    result = ''
    while point - 6 > 0:
        if bit[point-5:point+1] in password:
            # 원래는 그냥 출력을 하고 싶은데
            # 뒤에서부터 조사중임
            # 최종 모양은 0 2
            # ' ' + 2 + result
            # ' ' + 0 + ' 2'
            # ' 0 2'
            result = ' ' + str(password[bit[point-5:point+1]]) + result
            # print(password[bit[point-5:point+1]], end=' ')

            # 패턴 찾았으니까 다음 패턴 조사
            # 문제 조건중에 암호패턴이 붙어있다고 했음.
            point -= 6
        else:
            # 못 찾은 상황에 대해서 다른 조건들
            # 더 만들어서 처리 할 수도 있을 것임..
            point -= 1
    print(result)
    print(result.lstrip())
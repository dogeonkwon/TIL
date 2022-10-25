import sys

n = sys.stdin.readline().strip()
ans = ''

for i in range(len(n)):
    m = int(n[i])

    tmp = ''

    while m != 0:
        tmp += str(m % 2)
        m //= 2

    if i != 0:
        while len(tmp) < 3:
            tmp += '0'

    ans += tmp[::-1]

if ans != '':
    print(ans)
else:
    print(0)

    # if i == '0':
    #     ans += '000'
    # elif i == '1':
    #     ans += '001'
    # elif i == '2':
    #     ans += '010'
    # elif i == '3':
    #     ans += '011'
    # elif i == '4':
    #     ans += '100'
    # elif i == '5':
    #     ans += '101'
    # elif i == '6':
    #     ans += '110'
    # elif i == '7':
    #     ans += '111'

# if ans == '000':
#     print('0')
# else:
#     print(ans.lstrip('0'))

num = 10                    # 2진수, 8진수 변환
binary = ''
while num != 0:
    binary = str(num % 2) + binary          # 나누는 숫자를 2나 8로 바꾸면 2진수, 8진수로 표현가능
    num //= 2                               # 16진수는 따로 만들어야 할듯
print(binary)


result = 0                      # 10진수로 변환하기
for i in range(len(binary)):
    result = result * 2 + int(binary[i])
print(result)


num2 = 10
# 2진법 변환
binary2 = bin(num2)
print(binary2)
print(binary2.replace('0b', ''))


# 8진법 변환
octal = oct(num2)
print(octal)
print(octal.replace('0o', ''))


# 16진법 변환
hexademical = hex(num2)
print(hexademical)
print(hexademical.replace('0x', ''))


# 2진법을 10진법으로 변환
dec = int(binary, base=2)
print(dec)


text = '0b1010'
print(int(text, base=2))


text = '1010'
print(int(text, base=2))
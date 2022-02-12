### 1. 숫자의 의미

정수로 이루어진 list를 전달 받아, 각 정수에 대응되는 아스키 문자를 이어붙인 문자열을 반환하는 get_secret_word 함수를 작성하시오. 단, list는 65이상 90이하 그리고 97이상 122이하의 정수로만 구성되어 있다.

```python
def get_secret_word(words):
    total = ''				# str을 받아야 하기 때문에 처음 빈 값을 잡아준다.
    for word in words:		
        total += chr(word)  # -> chr : 정수(숫자)를 유니코드(문자)로 출력
    return total


print(get_secret_word([83, 115, 65, 102, 89])) #=> 'SsAfY'
```



---

### 2. 내 이름은 몇일까?

문자열을 전달 받아 해당 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 반환하는 get_secret_number 함수를 작성하시오. 단, 문자열은 A~Z, a~z로만 구성되어 있다.

```python
def get_secret_number(words):
    total = 0				# int를 받아야 하기 때문에 처음 값으 0으로 잡아준다.
    for word in words:
        total += ord(word)	# -> ord : 유니코드(문자)를 10진수(숫자)로 출력
        
    return total

print(get_secret_number('tom'))
```





---

### 3. 강한 이름

문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하 여 더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오.

```python
def get_strong_word(words1, words2):
    num1 = 0		# words들의 ord값을 받기 위한 변수
    num2 = 0

    for word1 in words1:		
        num1 += ord(word1)		# word1의 ord값을 num1에 저장해주면서 총합을 알게된다.
    
    for word2 in words2:
        num2 += ord(word2)
    
    if num1 > num2:
        return words1		# 문자를 출력해야하기 때문에 words1을 return 한다.
    else:
        return words2

print(get_strong_word('z', 'a'))
print(get_strong_word('tom', 'john'))
```
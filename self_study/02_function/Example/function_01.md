

**문제 1) **Python에서 기본으로 사용할 수 있는 built-in 함수를 최소 5가지 이상 작성하시오.



code

```python
abs(), enumerate(), len(), range(), min(), max()
```



---



**문제 2) **문자열을 전달 받아 해당 문자열의 정중앙 문자를 반환하는 get_middle_char 함수를
작성하시오. 단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 반환한다.



code

```python
# 첫 번째 풀이

def string_length(str):
    cnt = 0
    for i in str:
        cnt += 1
    return cnt

def string_middle(words):
    if string_length(words) % 2:
        return words[string_length(words)//2]
    else:
        return words[string_length(words)//2 - 1 : string_length(words) // 2 + 1]


print(string_middle(''))


# 두 번째 풀이

def get_middle_char(chars):
    cnt = 0				# 우선 문자열의 길이를 잰다.
    for char in chars:
        cnt += 1
        
    if cnt % 2:								# string[숫자]를 하면 그 숫자에 맞는 문자열이 나온다
        print(chars[cnt // 2])				# 홀수 문자이므로 // 2를 해준다.
    else:        							
        print(chars[cnt//2 -1:cnt//2+1])	# 짝수이므로 //2 - 1 슬라이싱 //2 + 1을 해준다

get_middle_char('ssafy') #=> a
get_middle_char('coding') #=> di
```

- `len()` 함수를 이용하지 않고 만들어 보려고 했는데 쉽지 않았다. 어떻게 만들었지만 다시 보면 아직 좀 어색하다.



---



**문제 3) **다음과 같이 함수가 선언되어 있을 때, 보기 (1)~(4) 중에서 실행 시 오류가 발생하는
코드를 고르시오.



code

```python
# 4번, ssafy(name = '길동', '구미') 를 했는데 처음 직접 대입을 했으면 계속 대입을 해야한다. 하지만 처음 위치에 맞게 했다가 나중에 대입하는 건 상관없다.

# => Keyword Argument 다음에 Positional Argument를 활용할 수 없다.
```

- 키워드 인자를 사용한 뒤에 위치 인자를 활요할 수 없다.



---



**문제 4) ** 다음과 같이 함수를 선언하고 호출하였을 때, 변수 result에 저장된 값을 작성하시오.



code

```python

# def my_func(a, b):
#    c = a + b
#    print(c)

# result = my_func(3, 7)

print(result)    # 낚이지 않게 조심하자. result에 저장된 값을 알기 위해서는 print(result)를 실행하					면 된다.

				# => None
```



---



**문제 5) ** 가변 인자 리스트를 사용하여, 갯수가 정해지지 않은 여러 정수들을 전달 받아 해당 정
수들의 평균 값을 반환하는 my_avg 함수를 작성하시오



code

```python
# 첫 번째 풀이
def my_avg(*numbers):
    cnt = 0
    total = 0
    for i in numbers:
        cnt += 1
        total += i

    print(total / cnt)

result = my_avg(77, 83, 95, 80, 70)

# 두 번째 풀이
def my_avg(*x):
    cnt = 0
    summ = 0

    for i in x:
        cnt += 1
        summ += i

    print(summ/cnt)

my_avg(77, 83, 95, 80, 70)

# 첫 번째 풀이와 두 번째 풀이가 별로 달라진 건 없다.
```


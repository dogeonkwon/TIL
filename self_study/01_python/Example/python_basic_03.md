1. Mutable & Immutable

- 주어진 컨테이너들을 각각 변경 가능한 것(mutable)과 변경 불가능한 것(immutable)으로 분류하시오.

  ```
  String, List, Tuple, Range, Set, Dictionary
  ```

```python
# mutable = > List, Set, Dictionary
# immutable = > String, Tuple, Range
```



- - 변경가능한 객체(mutable)에는 리스트(list)와 딕셔너리(dic)이 있다.
  - 변경불가능한 객체(immutable)에는 일반적인 자료형, int, string, tuple등이 있다.







2. 홀수만 담기

- range와 slicing을 활용하여 1부터 50까지의 숫자 중, 홀수로만 이루어진 리스트를 만드시오.

```python
# 리스트로 잡기 위해 j를 선언하였다.

j = []

# 1~51까지 홀수를 추출하고 append함수로 j에 넣어주었지만 append 함수를 사용하지 않도록 노력해야 겠다.

for i in range(1, 51)[::2]:
    j.append(i)

print(j)
```

```python
# list로 range를 묶었다.
# 위의 식보다 보기도 편하고 append함수를 사용하지 않았다.

j = list(range(1, 51))

print(j[::2])
```



---



3. Dictionary 만들기

- 반 학생들의 정보를 이용하여 key는 이름, value는 나이인 dictionary를 만드시오.

```python
# 처음에는 일일히 key와 value값을 맞춰주었다.
# dct = {'도건' : 24, '승연' : 23, '승현' : 22, '태엽' : 21}

# 두 번째는 dict함수를 이용하였다.
dt = dict(도건 = 20, 승연 = 21, 승현 =22, 태엽 = 23)

print(dt)
```



---



4. 반복문으로 네모 출력

- 두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 별(*) 문자를 이용하여 출력하시오. 단, 반복문을 사용하여 작성하시오

```python
# if를 이용하여 품

n = int(input())
m = int(input())

if n > 0:
    print('*'*n)
for i in range(1, m+1):
    if m > 0:
        print('*   *', sep='\n')
if n > 0:
    print('*'*n)
    
---------------------------------------------  

# 이 후에 while문을 사용하려 해결
n = 5
m = 9

i = 1 	# 시작값을 1로 하기위해 i, j변수를 1로 잡는다.
j = 1
while i <= m: 	# 세로의 길이를 밖에서 구해준다.
    i += 1
    while j < n: 	# 가로의 길이를 안에서 구해준다. => 가로 한 줄을 출력하고 이 후 세로 줄의 갯			j += 1										수대로 출력
    print(j * '*')
    
```



---



5. 조건 표현식

- 주어진 코드의 조건문을 조건 표현식으로 바꾸어 작성하시오

```python
temp = 36.5

print('입실 불가') if temp >= 37.5 else print('입실 가능')
```



---



6. 평균 구하기

- 주어진 list에 담긴 숫자들의 평균값을 출력하시오.

```python
# 답지 
score = [80, 89, 99, 83]

result = 0

for val in score:
    result += val

print('평균값은 : {}' .format(result/len(score)))


# len함수를 이용하지 않고 품
scores = [80, 89, 99, 83]

total = 0
cnt = 0

for i in scores:
    total += i
    cnt += 1
aver = total / cnt

print(aver)
```

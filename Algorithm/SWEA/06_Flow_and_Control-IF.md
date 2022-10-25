### 6. Flow and Control - IF(흐름과 제어 - IF)



**문제 1) **

```
다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오
```

input

```
9
```

output

```
1(은)는 9의 약수입니다.

3(은)는 9의 약수입니다.

9(은)는 9의 약수입니다.
```

code

```python
a = int(input())

for i in range(1, a+1):
    if a % i == 0:
        print("{}(은)는 {}의 약수입니다." .format(i, a))
```

- 이 문제를 풀면서 for문을 처음 사용해봤다. 여러 문법을 같이 사용하는 건 아직 익숙치 않은데 빨리 익숙해지도록 노력해야 겠다.



---



**문제 2) **

```
다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오.(단, 약수가 2개일 경우 소수임을 나타내십시오)
```

input

```
5
```

output

```
1(은)는 5의 약수입니다.
5(은)는 5의 약수입니다.
5(은)는 1과 5로만 나눌 수 있는 소수입니다.
```

code

```python
a = int(input())
cnt = 0

for i in range(1, a+1):
    if a % i == 0:
        print("{}(은)는 {}의 약수입니다." .format(i, a))
        cnt += 1
if cnt == 2:
    print("{}(은)는 1과 {}로만 나눌 수 있는 소수입니다." .format(a, a))
```

- 조금 헷갈린 문제였다. 변수 하나만 추가되어도 복잡하게 느껴지니 공부를 더 해야겠다.
- SWEA에는 결과값이 제대로 나오는데 파이참에서는 결과값이 제대로 안나와서 교수님에게 물어보기까지 했다. 알고보니 내가 다른 파일을 실행시키고 있었던 것이었는데 교수님께 정말 죄송스러웠다... 그리고 %d 도 사용하지만, SWEA에서 시험을 볼때는 print('{}' .format(변수)) 포맷을 더 많이 사용하는 습관을 들이는 것이 좋다고 말씀해주셨다. 다른 곳에서 개발을 할 때는 딱히 상관없다고도 덧붙여 말씀해 주셨다.



---



**문제 3) **

```
다음의 결과와 같이 입력된 영어 알파벳 문자에 대해 대소문자를 구분하는 코드를 작성하십시오.
```

input

```
b
```

output

```
b 는 소문자 입니다.
```

code

```python
a = input()
if 'a'<= a <= 'z':
    print('{} 는 소문자 입니다.'.format(a))
elif 'A'<= A <= 'Z':
    print('{} 는 대문자 입니다.'.format(a))
```

- 문자에 부등호를 이용한 건 처음이라 어색했다.



---



**문제 4) **

```
다음의 결과와 같이 가상의 두 사람이 가위 바위 보 중 하나를 내서 승패를 가르는 가위 바위 보 게임을 작성하십시오.
 
이 때 ["가위", "바위", "보"] 리스트를 활용합니다.
```

input

```
두 줄에 ["가위", "바위", "보"] 중 하나가 차례로 주어진다.
```

output

```
첫 번째 사람은 Man1, 두 번째 사람은 Man2라고 하고, 이긴 사람의 결과를 출력한다.

예를 들어, Man1이 이겼을 경우 Result : Man1 Win! 이라고 출력한다.

단, 비긴 경우는 Result : Draw 라고 출력한다.
```

code

```python
man1 = input()
man2 = input()
list = ['가위', '바위', '보']

if list.index(man1) < list.index(man2):
    if list.index(man1) == 0 and list.index(man2) == 2:
        print('Result : Man1 Win!')
    else:
        print('Result : Man2 Win!')
if list.index(man1) > list.index(man2):
    if list.index(man1) == 2 and list.index(man2) == 0:
        print('Result : Man2 Win!')
    else:
        print('Result : Man1 Win!')
if list.index(man1) == list.index(man2):
    print('Result : Draw')
```

- index를 이용해서 풀어봤는데 여전히 어렵다.



---



**문제 5) **

```
다음의 결과와 같이 입력된 문자가 대문자일 경우 소문자로, 소문자일 경우 대문자로 변경하고,

알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오.

출력 시 아스키코드를 함께 출력합니다.
```

input

```
c
```

output

```
c(ASCII: 99) => C(ASCII: 67)
```

code

```python
a = input()
#소문자일경우
if a.islower():
   print("%s(ASCII: %d) => %s(ASCII: %d)" % (a, ord(a), a.upper(), ord(a.upper())))
#대문자일경우
elif a.isupper():
   print("%s(ASCII: %d) => %s(ASCII: %d)" % (a, ord(a), a.lower(), ord(a.lower())))
#알파벳이 아닐경우
else :
   print(a)
```

```python
a = input()
if a.islower():
    print('{}(ASCII: {}) => {}(ASCII: {})' .format(a, ord(a), a.upper(), ord(a.upper())))
elif a.isupper():
    print('{}(ASCII: {}) => {}(ASCII: {})' .format(a, ord(a), a,lowe(), ord(a.lower())))
else:
    print(a)
```



- 다음 함수를 이용하여 문자열이 대문자 또는 소문자로 구성되어있는지 확인할 수 있습니다.

  - isupper() : 모든 문자열이 대문자이면 True를 리턴, 그렇지 않으면 False를 리턴
  - islower() : 모든 문자열이 소문자이면 True를 리턴, 그렇지 않으면 False를 리턴

  

- 다음 함수를 이용하여 문자열을 모두 대문자로 또는 모두 소문자로 변환할 수 있습니다.

  - upper() : 모든 문자열을 대문자로 변경
  - lower() : 모든 문자열을 소문자로 변경

  

---



**문제 7)** 

```
1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자들을 찾아
콤마(,)로 구분된 문자열을 구성해 출력하는 프로그램을 작성하십시오.
```

input

```

```

output

```
7,14,21,28,42,49,56,63,77,84,91,98,112,119,126,133,147,154,161,168,182,189,196
```

code

```python
a = 1

while a <= 200:
    if a % 7 == 0 and a % 5 != 0:
        print(a, end = ',')
    a += 1
```

- 처음에는 이런 코드를 짰는데 마지막 196 뒤에 (,)콤마가 붙어서 오류가 났다.

```
a = 1

while a <= 200:
    if a == 196:
        print(a)
    elif a % 7 == 0 and a % 5 != 0:
        print(a, end = ',')
    a += 1
```

- 마지막 값이 196이라는 것을 알았기 때문에 꼼수를 부렸는데 어떤 코드를 짜야 제대로 풀 수 있는지 고민해봐야 겠다.



---



**문제 8)** 

```
100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아 콤마(,)로 구분해 출력하는 프로그램을 작성하십시오.
```

input

```

```

output

```
200,202,204,206,208,220,222,224,226,228,240,242,244,246,248,260,262,264,266,268,280,282,284,286,288
```

code

```python
for i in range(100, 301):
    if i == 288 : print(i)
    elif i % 2 == 0 and (i // 10) % 2 == 0 and (i // 100) % 2 == 0:
        print(i, end = ',')
```

- 테스트케이스가 많은 경우 문자열이나 리스트에 담는 방법으로 짜봐야 할 것 같다.



---


### 7. Flow and Control - Iteration



**문제 1) **

```
다음의 결과와 같이 5명의 학생의 점수에 대해 60 이상일 때 합격 메시지를 출력하고,

60미만일 때 불합격 메시지를 출력하는 프로그램을 만드십시오.
```

input

```

```

output

```
1번 학생은 88점으로 합격입니다.

2번 학생은 30점으로 불합격입니다.

3번 학생은 61점으로 합격입니다.

4번 학생은 55점으로 불합격입니다.

5번 학생은 95점으로 합격입니다.
```

code

```python
students = [88, 30, 61, 55, 95]
for student in range(len(students)):
    if students[student] >= 60:
        print('{}번 학생은 {}점으로 합격입니다.'.format(student+1, students[student]))
    else:
        print('{}번 학생은 {}점으로 불합격입니다.'.format(student+1, students[student]))
```



---



**문제 2) **

```
1부터 100까지의 숫자를 for 문과 range 함수를 이용해 출력하십시오.
```

input

```

```

output

```
1

2

3

4

5

...

99

100
```

code

```python
for i in range(1, 101):
    print(i)
```



---



**문제 3) **

```
1부터 100사이의 숫자 중 짝수를 for 문을 이용해 다음과 같이 출력하십시오.
```

input

```

```

output

```
2 4 6 8 10 12 14 16 18 ... 90 92 94 96 98 100
```

code

```python
for i in range(1, 101):
    if not i % 2:
        print(i, end = ' ')
```



---



**문제 4) **

```
1부터 100사이의 숫자 중 홀수를 for 문을 이용해 다음과 같이 출력하십시오.
```

input

```

```

output

```
1, 3, 5, 7, 9, ... 95, 97, 99
```

code

```python
ans = ''
for i in range(1, 101):
    if i % 2:
        ans += str(i) + ', '
print(ans[:len(ans) - 2])       # ', '는 str로 2글자라고 인식하기 때문에 끝에서 -2를 해줘야 `,` 앞까지만 출력된다.
```



---



**문제 5) **

```
1부터 100사이의 숫자 중 3의 배수의 총합을 for 문을 이용해 출력하십시오.
```

input

```

```

output

```
1부터 100사이의 숫자 중 3의 배수의 총합: 1683
```

code

```python
result = 0
for number in range(1, 101):
    if not number % 3:
        result += number
print('1부터 100사이의 숫자 중 3의 배수의 총합: {}'.format(result))
```



---



**문제 6)** 

```
다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.

['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.
```

input

```

```

output

```
{'A': 3, 'O': 3, 'B': 2, 'AB': 2}
```

code

```python
blood = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
cnt_a = 0
cnt_b = 0
cnt_o = 0
cnt_ab = 0
for i in blood:
    if 'A' == i:
        cnt_a += 1
    elif 'B' == i:
        cnt_b += 1
    elif 'O' == i:
        cnt_o += 1
    elif 'AB' == i:
        cnt_ab += 1

# 작은 따옴표를 넣는 것보다 {}(중괄호)를 표현하는 것이 까다로웠다. 처음에는 제일 뒤에 .format을 넣어서 자꾸 오류가 났고 .format의 위치를 바꿔 출력할 수 있다는 생각을 하게 되었다.
print('{'+"'A': {}, 'O': {}, 'B': {}, 'AB': {}".format(cnt_a, cnt_o, cnt_b, cnt_ab)+'}')  
```



```python
blood = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
dic = {}
for i in blood:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)
```

- 두 번째는 딕셔너리를 이용하여 풀었는데, 처음부터 생각나지 않았다. 계속 연습해야 겠다.



---



**문제 7) **

```
다음은 학생의 점수를 나타내는 리스트입니다.

[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.
```

input

```

```

output

```
454
```

code

```python
score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
i = 0
total = 0
cnt = 0
length = len(score)

# pop()함수를 사용할 때마다 리스트의 값이 삭제되면서 제 자리에 맞는 숫자를 비교하기 위해 삭제될 경우 삭제된 숫자만큼을 뜻하는 cnt를 빼줘서 코드를 작성하였다.
while i < length:
    if score[i-cnt] < 80:
        score.pop(i-cnt)
        cnt += 1
    else:
        total += score[i-cnt]
    i += 1
print(total)
```



```python
score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
num = 0

# i = score.pop() 하면 마지막 리스트가 제거 되면서 저장된다. 
# 그리고 if문으로 80 이상인 수를 뽑고 num에 더해준다.
while len(score) > 0:
    i = score.pop()
    if i >= 80:
        num += i
print(num)
```



---



**문제 8)**

```
while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
```

input

```

```

output

```
*****

****

***

**

*
```

code

```python
star = 5
while star > 0:
    print('*'*star)
    star -= 1
```



---



**문제 9)**

```
while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
```

input

```

```

output

```
*******

 *****

  ***

   *
```

code

```python
star = 7
blank = 0
while star > 0:
    print(' '*blank+'*'*star)
    star -= 2
    blank += 1
```



---



**문제 10)**

```
다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.
```

input

```
11
```

output

```
0 1 2 3 4 5 6 7 8 9

0 2 0 0 0 0 0 0 0 0
```

code

```python
numbers = input()
lst_cnt = [int(i*0) for i in range(10)]
num = 0

for i in range(10):
    print(i, end=' ')

for number in numbers:
    lst_cnt[int(number)] += 1

# 0~9를 표현해 줄 for문의 print와 그에 맞는 갯수를 출력해줄 for문의 print를 구분하기 위하여 중간에 print()를 넣었다.
print()

# 2번 째줄의 마지막 0에서 뒤에 띄어쓰기를 같이 출력해 오답이 나왔다. 마지막 띄어쓰기를 제거하기 위해 for문에 리스트를 넣는 것이 아니라 길이를 이용한 range로 구성하였다.
for j in range(len(lst_cnt)):
    if j == len(lst_cnt)-1:
        print(lst_cnt[j])
    else:
        print(lst_cnt[j], end=' ')
```



---



**문제 11)**

```
for문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
```

input

```

```

output

```
    *

   **

  ***

 ****

*****
```

code

```python
for i in range(1, 6):
    print(' ' * (5 - i) + '*' * i)
```



---



**문제 12)**

```
다음의 결과와 같이 10진수를 2진수로 변환하는 프로그램을 작성하십시오.
```

input

```
9
```

output

```
1001
```

code

```python
num = int(input())

# 값들을 차례대로 넣어줄 result를 생성해준다.
result = ''

# num이 1이 될 때까지는 이진법에 적용이 되므로 >= 1을 설정해주고 이진법이기 때문에 2로 나눈 나머지 값들을 차례대로 넣어준다. 그리고 뒤에 result값을 더해준다. 그렇게 하면 순서대로 출력을 할 수 있다. 또한 while의 종료문을 설정하기 위해 num // 2를 해준다.
while num >= 1:
    result = str(num % 2) + result
    num = num // 2
print(result)
```




### 1. 모음은 몇 개나 있을까?



**문제 1) **

```
문자열을 전달 받아 해당 문자열의 모음 갯수를 반환하는 count_vowels 함수를
작성하시오. 단, .count() 메서드를 활용하여 작성하시오.

```

``` python
count_vowels('apple') # => 2
count_vowels('banana') # => 3
```

code

```python
def count_vowels(x):

    vowels = 'aeiouAEIOU'       # 알파벳 소문자와 대문자를 따로 인식하기 때문에 aeiou(모음)의 소문자, 대문자를 같이 넣어준다.
    result = 0          # 갯수를 구해야 하기 때문에 result에 0을 넣어준다.
    for i in vowels:        
        result += x.count(i)        # for문을 돌리면서 모음이 있는지 하나씩 비교해준다.
    print(result)

count_vowels('apple')
count_vowels('banana')
```



---



### 2. 문자열 조작

**문제 2) ** 다음 중, 문자열(string)을 조작하는 방법으로 옳지 않은 것을 고르시오

```
(1) .find(x)는 x의 첫번째 위치를 반환한다. 없으면 -1을 반환한다.

(2) .split([chars])은 특정 문자를 지정하면 문자열을 특정 문자를 기준으로 나누어 list로 반환한다. 특정     문자를 지정하지 않으면공백을 기준으로 나눈다.

(3) .replace(old, new[, count])는 바꿀 대상 문자를 새로운 문자로 바꿔서 반환한다.

(4) .strip([chars])은 특정 문자를 지정하면, 양쪽에서 해당 문자를 찾아 제거한다. 특정 문자를 지정하지 않     으면 오류가 발생한다.
```



code

```python
# (4)번
# .strip([chars])는 특정한 문자들을 지정하면, 양쪽을 제거하거나(strip), 왼쪽을 제거하거나(lstrip), 오른쪽을 제거(rstrip) / 문자열을 지정하지 않으면 공백을 제거함
# 이라고 하는 것이 더 적절하다.
```





---



### 3. 정사각형만 만들기

**문제 3) **

```
각각 너비와 높이의 값으로 이루어진 2개의 list를 전달 받아, 각각의 값들을 조합하여 만들 수 있는 정사각형만의 넓이를 담은 list를 반환하는 only_square_area 함수를 작성하시오.
```



```python
only_square_area([32, 55, 63], [13, 32, 40, 55])

# => [1024, 3025]
```

code

```python
 def only_square_area(x, y):

     result = []
     for i in range(len(x)):
         for j in range(len(y)):
             if x[i] == y[j]:           # x[i] = y[j]가 같다면 정사각형의 넓이를 구할 수 있다.
                 result.append((x[i] * y[j]))

     return result


 print(only_square_area([32, 55, 63], [13, 32, 40, 55]))
```






### 1. Built-in 함수와 메서드



**문제 1) ** sorted()와 .sort()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

code

```python
numbers = [5, 4, 8, 1, 2]

numbers.sort()
print(numbers) # list.sort() 반환하는 값이 None이다. / reverse=True 하면 역순으로 나온다. / 다른 변수에 저장하지 않고 변수 그대로를 써서 사용한다.

lst = sorted(numbers) # sorted(list) 반환값이 정렬된 리스트이다. / reverse=True 하면 역순으로 나온다. / 다른 변수에 저장해서 사용해야 한다.
print(lst)
```



---



### 2. extend()와 .append()

**문제 2) ** .extend()와 .append()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

code

```python
numbers = [2, 6, 9, 4, 1]

numbers.append(7) # append는 리스트에 값을 추가하는 함수이다.
print(numbers)
# => [2, 6, 9, 4, 1, 7]

numbers.extend(['ediya']) # extend는 리스트에 iterable(list, range, tuple, string) 값을 붙일 수가 있습니다.
print(numbers)
# => [2, 6, 9, 4, 1, 7, 'ediya']

numbers.extend('ediya')  # extend 메서드로 'e', 'd', 'i', 'y', 'a' 를 하나씩 추가한다.
print(numbers)
# => [2, 6, 9, 4, 1, 7, 'ediya', 'e', 'd', 'i', 'y', 'a']
```





---



### 3. 복사가 잘 된 건가?

**문제 3) **아래의 코드를 실행 하였을 때, 변수 a와 b에 담긴 list의 요소가 같은지 혹은 다른지 여부를 판단하고 그 이유를 작성하시오.

```python
a = [1, 2, 3, 4, 5]
b = a

a[2] = 5

print(a)
print(b)
```

code

```python
a = [1, 2, 3, 4, 5]
b = a

a[2] = 5

print(id(a))    # => id를 출력했을 때 같은 값을 출력하기 때문에 같은 것을 참조한다.
print(id(b))

print(a)    # => a[2]를 5로 바꾸고 출력하였을 때도 a, b 다 숫자가 변해서 출력되는 것을 알 수 있다.
print(b)

# => 따라서 list의 요소가 같다.
```






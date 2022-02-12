**문제 1)** List의 합 구하기

정수로만 이루어진 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

```python
# 첫 번째 풀이(답지)

def list_sum(lst):
    
    total = 0
    for i in lst:
        total += i
    return print(total)

list_sum([1, 2, 3, 4, 5])

# 두 번째 풀이(혼자)
def list_sum(numbers):
    summ = 0

    for i in numbers:
        summ += i

    print(summ)

list_sum([1, 2, 3, 4, 5])  # => 15
```

---

**문제 2)** Dictionary로 이루어진 List의 합 구하기

Dictionary로 이루어진 list를 전달 받아 모든 dictionary의 'age' key에 해당하는 value 들의 합을 반환하는 dict_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

```python
# 첫 번째 풀이(답지)

def le(ls):
    cnt = 0
    for i in ls:
        cnt += 1
    return cnt


def dict_list_sum(lst_sum):

    total = 0

    for i in range(le(lst_sum)):
        lst = lst_sum[i]
        total += lst['age']

    print(total)
    
    dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}])
    
# 두 번째 풀이(혼자)

def dict_list_sum(lst):
    cnt = 0					# 길이를 구한다.
    for i in lst:
        cnt += 1

    summ = 0
    i= 0
    while i < cnt:						# 2 미만의 값들을 추출한다.
        summ += int(lst[i]['age'])		# list[][]함수를 적절하게 이용한다.
        i += 1
    print(summ)


dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}])
```

---

**문제 3) **2차원 List의 전체 합 구하기

정수로만 이루어진 2차원 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 all_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오

```python

# 첫 번째 풀이(답지)
def le(ls):
    cnt = 0
    for i in ls:
        cnt += 1
    return cnt

def all_list_sum(lst):


    total = 0

    for i in range(le(lst)):
        for j in range(le(lst[i])):

            total += lst[i][j]
    print(total)



all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])


# 두 번째 풀이(혼자)

def all_list_sum(lst):

    cnt = 0
    for i in lst:		# 갯수를 구하기 위해 cnt 함수를 잡아준다.
        cnt += 1

    summ = 0

    for i in range(cnt):		# cnt까지 for문을 돌릴 수 있게 range()를 썼지만 나중에 다른 									방법을 찾아봐야 겠다.
        j = 0					
        for j in range(i+1):	
# 처음에 range()안에 i를 넣어서 안 됐다. 그 이유가 i가 첫 번째에는 0이기 때문에 for문이 동작하지 않고 그냥 생략됐다. 그래서 처음부터 동작하도록 '+1'을 넣었다.
            summ += lst[i][j]	# 이 후는 리스트에 맞는 결과값을 도출해내 합을 구한다.
    print(summ)


all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])
```
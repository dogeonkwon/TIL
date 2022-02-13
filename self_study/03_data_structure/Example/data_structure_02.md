### 1. 평균 점수 구하기

**문제 1) **key 값으로 과목명, value 값으로 점수를 가지는 dictionary를 전달 받아, 전체 과목의 평균 점수를 반환하는 함수 get_dict_avg 함수를 작성하시오.

```python
print(get_dict_avg({
    'python' : 80,
    'algorithm' : 90,
    'django' : 89,
    'web' : 83,
}))
```



code

```python
def get_dict_avg(x):
    
    total = 0
    cnt = 0
    
    # for key in x.keys(): <- x함수의 key값만 추출한다.
    # for val in x.values(): <- x함수의 values 값만 추출한다.
    # for key, val in x.items(): <- x함수의 key값과 value값을 추출한다.

    for val in x.values():      
        total += val
        cnt += 1
    return total / cnt

print(get_dict_avg({
    'python' : 80,
    'algorithm' : 90,
    'django' : 89,
    'web' : 83,
}))  # => 85.5
```



---



### 2. 혈액형 분류하기

**문제 2) **여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아, key는 혈액형의 종류, value는 사람 수인 dictionary를 반환하는 count_blood 함수를 작성하시오.

```python
print(count_blood(['A', 'B', 'A', 'O', 'AB', 'AB', 
            'O', 'A', 'B', 'O', 'B', 'AB',
])) # => {'A' : 3, 'B' : 3, 'O' : 3, 'AB' : 3}
```



code

```python
def count_blood(bloods):
    
new = dict()
    for i in bloods:
        if new.get(i):      # new 딕셔너리에 i값이 있다면 값에 +1을 해주고 
            new[i] += 1
        else:               # 없다면 1을 만들어 주라
            new[i] = 1
    return new

print(count_blood(['A', 'B', 'A', 'O', 'AB', 'AB', 
            'O', 'A', 'B', 'O', 'B', 'AB',
])) # => {'A' : 3, 'B' : 3, 'O' : 3, 'AB' : 3}
```





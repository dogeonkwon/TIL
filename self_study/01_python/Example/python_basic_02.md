### 1. 세로로 출력하기

자연수 number를 입력 받아, 1부터 number까지의 수를 세로로 한줄씩 출력하시오.

```python
num = int(input())
i = 1
while i <= num:		# 처음에 10미만의 값을 넣어서 9까지만 출력되었다. 
    print(i)
    i += 1
```



---



### 2. 거꾸로 세로로 출력하기

자연수 number를 입력 받아, number부터 0까지의 수를 세로로 한줄씩 출력하시오.

```python
num = int(input())

while num >= 0:		# 입력한 값이 1 씩 줄어들면서 0까지 출력되야 한다.
    print(num)
    num -= 1
```



---



### 3. N줄 덧셈 (SWEA #2025)

입력으로 자연수 number가 주어질 때, 1부터 주어진 자연수 number까지를 모두 더한 값 을 출력하시오. 단, 주어지는 숫자는 10000을 넘지 않는다. 예를 들어, 주어진 숫자가 10일 경우 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55이므로, 출력해야 할 값은 55이다.

```python
num = int(input())

i = 1
total = 0

while i <= num:			# 1부터 입력한 num 값만큼 더해줘야 하기때문에 i <= num을 사용하였다.
    total += i			
    i += 1

print(total)
```
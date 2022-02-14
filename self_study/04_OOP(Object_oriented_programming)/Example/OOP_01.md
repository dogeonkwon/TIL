### 1. Type Class

**문제 1) **Python은 객체 지향 프로그래밍 언어이다. Python에서 기본적으로 정의되어 있는 클래스를 최소 5가지 이상 작성하시오.

code

```python
int, str, float, list, set, memoryview
```



---



### 2. Magic Method

**문제 2) **아래에 제시된 매직 메서드들이 각각 어떠한 역할을 하는지 간단하게 작성하시오.

```python
__init__, __del__, __str__, __repr__
```



code

```python
__init__ : 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드

__del__ : 인스턴스 객체가 소멸되기 직전에 호출되는 메소드
    
__str__ : 해당 객체의 출력 형태를 지정
    
__repr__ : 시스템이 인식하는 대로, 객체의 모습 그대로를 호출
    
```



### 3. Instance Method

**문제 3) **.sort()와 같이 문자열, 리스트, 딕셔너리 등을 조작 할 때 사용하였던 것들은 클래스에 정의된 메서드들이었다. 이처럼 문자열, 리스트, 딕셔너리 등을 조작하는 메서드를 최소 3가지 이상 그 역할과 함께 작성하시오.



code

```python
.append() 메소드 : 선택된 요소의 마지막에 새로운 HTML 요소나 콘텐츠를 추가한다.

.prepend() 메소드 : 선택한 요소의 첫번째에 새로운 요소나 콘텐츠를 추가한다.

.before() 메소드 : 선택한 요소의 '바로 앞쪽에' 새로운 요소나 콘텐츠를 추가한다.
   
.after() 메소드 : 선택한 요소의 '바로 뒤쪽에' 새로운 요소나 콘텐츠를 추가한다.

.wrap() 메소드 : '선택한 요소'를 감싸는 새로운 요소를 추가한다.
```



### 4. Module Import

```python
# fibo.py

def fibo_recursion(n):
	if n < 2:
		return n
	else:
		return fibo_recursion(n-1) + fibo_recursuion(n-2)
```

**문제 4)** 위와 같은 코드가 같은 폴더 안의 fibo.py 파일에 작성되어 있을 때, 아래와 같은 형태로 함수를 실행 할 수 있도록 하는 import 문을 빈칸 (a), (b), (c)를 채워 넣어 완성하시오



```python
from __(a)__ import __(b)__ as __(c)__

recursion(4)

(a) : fibo
(b) : fibo_recursion
(c) : recursion
```



---



- **모듈(module) :** 특정 기능을 .py 파일 단위로 작성한 것
- **패키지(package) :** 특정 기능과 관련된 여러 모듈을 묶은 것
- **파이썬 표준 라이브러리(library) :** 파이썬에 기본으로 설치된 모듈과 패키지



> mport 모듈
> import 모듈1, 모듈2
>
> 모듈.변수
> 모듈.함수()
> 모듈.클래스()

모듈은 import를 통해 가져올 수 있으며, 해당 모듈의 변수, 함수, 클래스를 이용할 수 있다.

아래는 **math 모듈의 pi 변수와 squrt 함수**를 활용한 예시

```python
>> import math

>> math.pi
3.141592653589793
>> math.sqrt(3.0)
1.7320508075688772
```



> import 모듈 as 이름

항상 math 모듈을 타이핑하는 **번거로움을 as 를 통해 해결**할 수 있다.

아래는 **math 모듈을 m으로 지정**해 번거로움을 줄인 예시

```python
>> import math as m

>> m.pi
3.141592653589793
>> m.sqrt(3.0)
1.7320508075688772
```



### from import로 모듈의 일부만 가져오기

> from 모듈 import 변수
> from 모듈 import 함수
> from 모듈 import 클래스
> from 모듈 import *

변수,함수 그리고 클래스를 조금더 편리하게 사용하는 방법이 있다.

**math 모듈에서 변수 pi와 sqrt만** 가져오려면 **from import를 사용하면 math나 m을 붙이지 않고 바로 사용**할 수 있다.

```python
>> from math import pi,sqrt

>> pi
3.141592653589793
>> sqrt(3.0)
1.7320508075688772
```

만약 모듈안의 모든 변수와 함수들을 편리하게 이용하고 싶다면 다음과 같이 *를 활용하면 된다.

```python
>> from math import *

>> pi
3.141592653589793
>> sqrt(3.0)
1.7320508075688772
```


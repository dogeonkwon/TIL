

# OOP(Object_oriented_programming)

## 개요

- #### 객체지향 프로그래밍(OOP)

  - oop 기초
  - 인스턴스
  - 클래스
  - 메소드

- #### 객체지향의 핵심개념

  - 추상화
  - 상속
  - 다형성
  - 캡슐화

---

## 객체지향 프로그래밍

- ####  객체

  - ***파이썬은 모두 객체(object)로 이뤄져 있다.***

  - 객체는 특정 타입의 인스턴스(instance) 이다.
    - 123, 900, 5는 모두 int의 인스턴스
    - 'hello', 'bye'는 모두 string의 인스턴스
    - [231, 99, 2], []은 모두 list의 인스턴스

  - 객체의 특징
    - 타입(type) : 어떤 연산자(operator)와 조작(method)가 가능한가?
    - 속성(attribute) : 어떤 상태(데이터)를 가지는가?
    - 조작법(method) : 어떤 행위(함수)를 할 수 있는가


![image-20220126072853644](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220126072853644.png)



- 객체 **지향** 프로그래밍이란?
  - 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍방법
- ***예시(시각화)***
  - 콘서트
    - 가수 객체
    - 감독 객체
    - 관객 객체

---

- 절차지향 -> 객체지향(패러다임의 변화)
  - sorted와 sort의 차이를 봐도 알 수 있다.

```python
# 절차지향의 구조

a = [1, 2, 3]

a = sorted(a)		# => a에 a를 sorted한 결과를 넣어준다.

a = resversed(a)

def append(1, value):
    return 1 + [value]

a = append(a, 4)
```



```python
# 객체지향의 구조

a = [1, 2, 3]

a.sort(a)		# => a에 직접 sort를 사용한다.

a.resverse()

a.append(4)
```



#### - 절차지향 프로그래밍 -

![image-20220126073045141](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220126073045141.png)



#### - 객체지향 프로그래밍 - 

![image-20220126073102191](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220126073102191.png)



- ***예시(추상화)***

![image-20220126073150778](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220126073150778.png)





#### 예시 ) 사각형 넓이 구하기 코드

![image-20220126074008386](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220126074008386.png)



![image-20220126074121700](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220126074121700.png)

![image-20220126074138079](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220126074138079.png)

---

![image-20220126074058613](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220126074058613.png)



## OOP 기초

- 기본 문법
  - 사각형 - **클래스(class)** : class Myclass:
  - 각 사각형(R1, R2) - **인스턴스(instance)** : my_instance = MyClass()
  - 사각형의 정보 - **속성(attribute)** : my_instance.my_method()
    - 가로 길이, 세로 길이
  - 사각형의 행동 - **메소드(method)** : my_instance.my_attribute
    - 넓이를 구한다. 높이를 구한다.

![image-20220130164807689](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130164807689.png)

---

- ==
  - 동등한(equal)
  - 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True
  - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님
- is
  - 동일한(identical)
  - 두 변수가 동일한 객체를 가리키는 경우 True

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b, a is b)

# => True, False
```

```python
a = [1, 2, 3]
b = a

print(a == b, a is b)

# => True, True
```

- if a is None: 이 올바른 표현

---

## 인스턴스

- 인스턴스 변수란?
  - 인스턴스가 개인적으로 가지고 있는 속성
- 생성자 메소드에서 `self.<name>`으로 정의
- 인스턴스가 생성된 이후 `<instance>.<name>`으로 접근 및 할당

- #### 호출 시, 첫번째 인자로 ***인스턴스 자기자신(self)이 전달됨***

  - self대신 다른 단어로 써도 작동하지만 바꾸지 않는 것이 파이썬의 암묵적인 규칙

- 파이썬에서 인스턴스 메소드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계

```python
# 클래스 정의 (Person)
class Person:
    # 인스턴스 메서드
    # Python 내부적으로 person.test(p1) 
    def test(self):
        return self
    
# 인스턴스 생성 (p1)
p1 = Person()

# p1.test()
# TypeError : test() takes 0 positional arguments but 1 was given

# <__main__.Person object at 0x00
# Python 내부적으로 Person.test(p1)
s = p1.test()
p1.test(s, p1)
```

---

- 생성자(constructor) 메소드
  - 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
  - 인스턴스 변수들의 초기값을 설정
    - 인스턴스 생성
    - `__init__` 메소드 자동 호출

![image-20220126123832323](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220126123832323.png)

---

- 소멸자 메소드
  - 인스턴스 객체가 소멸되기 직전에 호출되는 메소드

![image-20220126123854274](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220126123854274.png)

---

- 매직 메소드

  - Double underscore(_)가 있는 메소드는 특수한 동작을 위해 만들어진 메소드로, 특정 상황에 자동으로 불리는 메소드
  - `__str__` : 해당 객체의 출력 형태를 지정
    - 프린트 함수를 호출할 때, 자동으로 호출
  - `__init__` : 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
  - `__len__` : 문자열의 길이를 반환
  - `__repr__` : 시스템이 인식하는 대로, 객체의 모습 그대로를 호출
  - `__lt__` : < 비교
  - `__le__` : <= 비교
  - `__eq__` : == 작업
  - `__gt__` : > 비교
  - `__ge__` : >= 비교
  - `__ne__` : != 작업

![image-20220126124322255](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220126124322255.png)

---

## 클래스

#### 클래스 변수

- 클래스 속성
  - 한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성
- `<classname>.<name>` 으로 접근 및 할당

![image-20220126124413170](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220126124413170.png)

---

#### 클래스 메소드

- 클래스가 사용할 메소드
- `@classmethod` 데코레이터를 사용하여 정의
  - 데코레이터 : 함수를 어떤 함수로 꾸며서 새로운 기능을 부여

![image-20220126124618504](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220126124618504.png)

---

#### 스태틱 메소드

- 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드로 속성을 다루지 않고 단지 기능(행동)만을 하는 메소드를 정의할 때, 사용
- `@staticmethod` 데코레이터를 사용하여 정의

![image-20220126124747582](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220126124747582.png)

---

- #### 인스턴스와 클래스 간의 이름 공간(namespace)

  - 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
  - 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
  - 인스턴스에서 특정 속성에 접근하면, 인스턴스 - 클래스 순으로 탐색 

![image-20220126124855737](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220126124855737.png)



## 메소드 정리

![image-20220130165148885](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130165148885.png)

- #### 인스턴스 메소드

  - self 매개변수를 통해 동일한 객체에 정의된 속성 및 다른 메소드에 자유롭게 접근 가능
  - 클래스자체에도 접근 가능 -> 인스턴스 메소드가 클래스 상태를 수정할 수도 있음

- #### 클래스 메소드

  - 클래스를 가리키는 cls 매개 변수를 받음
  - cls 인자에마 접근할 수 있기 때문에 객체 인스턴스 상태를 수정할 수 없음

- #### 스태틱 메소드

  - 임의개수의 매개변수를 받을 수 있지만, self나 매개변수는 사용하지 않음
  - 객체 상태나 클래스 상태를 수정할 수 없음
  - 일반 함수처럼 동작하지만 클래스의 이름공간에 귀속 됨
    - 주로 해당 클래스로 한정하는 용도로 사용

---

![image-20220130165542002](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130165542002.png)



![image-20220130165553842](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130165553842.png)



![image-20220130165610661](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130165610661.png)



![image-20220130165634119](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130165634119.png)

---

## 객체 지향의 핵심개념

- ### 추상화

![image-20220130165712664](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130165712664.png)



![image-20220130165727573](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130165727573.png)



![image-20220130165741119](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130165741119.png)

---

- ### 상속

  - 두 클래스 사이 부모 - 자식 관계를 정립하는 것 
  - 클래스는 상속이 가능함
    - 모든 파이썬 클래스는 object를 상속 받음

```python
class ChildClass(ParentsClass)
```

- 부모클래스의 속성, 메소드가 자식 클래스에 상속되므로, 코드 재사용성이 높아짐
- 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속 받음

![image-20220130165949365](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130165949365.png)

---

- `isinstance(object, classinfo)`
  - classinfo의 instance거나 subclass*인 경우 True

![image-20220130170532510](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130170532510.png)



![image-20220130170629674](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130170629674.png)

---

- super()
  - 자식클래스에서 부모클래스를 사용하고 싶은 경우

![image-20220130170711177](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130170711177.png)

---

### 상속 정리

- 파이썬의 모든 클래스는 object로부터 상속됨
- 부모 클래스의 모든 요소(속성, 메소드)가 상속됨
- super()를 통해 부모 클래스의 요소를 호출할 수 있음

- 메소드 오버라이딩을 통해 자식클래스에서 재정의 가능함
- 상속관계에서의 이름 공간은 **인스턴스 -> 자식 클래스 -> 부모 클래스** 순으로 탐색

---

#### 다중 상속

- 두개 이상의 클래스를 상속 받을 경우

- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

- mro 메소드 (Method Resolution Order)
  - g해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메소드
  - **기존의 인스턴스 -> 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 -> 자식 클래스 -> 부모 클래스로 확장**
  
  
  
  ![image-20220130171531241](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130171531241.png)



![image-20220130171545555](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130171545555.png)

---

- ### 다형성

  - 동일한 메소드가 클래스에 따라 다르게 행동할 수 있음을 의미

  - 서로 다른 클래스에 속해있는 객체들이 **동일한 메시지에 대해 다른 방식으로 응답될 수 있음**

- **메소드 오버라이딩**
  - 상속 받은 메소드를 재정의
  - 클래스 상속 시, 부모 클래스에서 정의한 메소드를 자식 클래스에서 변경
  - 부모 클래스의 메소드를 실행시키고 싶은 경우 super를 활용

![image-20220130172052296](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130172052296.png)

---


- ### 캡슐화

  - 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단
  - 파이썬에서 암묵적으로 존재하지만, 언어적으로는 존재하지 않음

#### 	접근제어자 종류

- Public Access Modifier : 어디서나
- Protected Access Modifier : 상속 관계
- Private Access Modifier : 본인

 

#### 	Public Member

- 언더바 없이 시작하는 메소드나 속성
- 어디서나 호출이 가능, 하위클래스 override 허용

![image-20220130172228759](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130172228759.png)

---

#### 	Protected Member

- 언더바 1개로 시작하는 메소드나 속성
- 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능
- 하위 클래스 override 허용

![image-20220130172304104](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130172304104.png)

---

#### 	Private Member

- **언더바 2개**로 시작하는 메소드나 속성
- 본 클래스 내부에서만 사용이 가능
- 하위클래스 상속 및 호출 불가능(오류)
- 외부 호출 불가능(오류)

![image-20220130172334124](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130172334124.png)

---

#### 	getter 메소드와 setter 

- 변수에 접근할 수 있는 메소드를 별도로 생성
  - getter 메소드 : 변수의 값을 읽는 메소드
    - @property 데코레이터 사용
  - setter 메소드 : 변수의 값을 설정하는 성격의 메소드 
    - @변수.setter 사용



![image-20220130172424673](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130172424673.png)



---

---

---



## homework_07

### 문제 4) 

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

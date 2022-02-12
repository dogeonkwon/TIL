# 함수

### 개요

- 함수 기초
- 함수의 결과값(Output)
- 함수의 입력(Input)
- 함수의 범위(Scope)
- 함수의 문서화(Doc-string)
- 함수 응용

## 함수 기초

- 함수(Function)
  - 특정한 기능을 하는 코드의 조각(묶음)
  - 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 간편히 사용

![image-20220129214125253](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129214125253.png)

- 함수의 정의 
  - 상용자 함수(Custom Function)
    - 구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성 가능

![image-20220129214219250](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129214219250.png)

---

![image-20220129214257470](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129214257470.png)

---

- 내장함수(Built-in Function) 활용

![image-20220129214431042](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129214431042.png)

---

- pstdev 함수 (파이썬 표준 라이브러리 - statistics)

![image-20220129214512947](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129214512947.png)

---

### 함수 기본 구조

- 선언과 호출(define & call)
- 입력(Input)
- 문서화(Doc-String)
- 범위(Scope)
- 결과값(Output)

![image-20220129214636374](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129214636374.png)

---

- 선언과 호출(define & call)
  - 함수의 선언은 def 키워드를 활용함
- 들여쓰기를 통해 Function body(실행될 코드 블록)를 작성함
  - Docstring은 함수 body 앞에 선택적으로 작성 가능
    - 작성시에는 반드시 첫 번째 문장에 문자 "' "'
- 함수는 parameter를 넘겨줄 수 있음
- 함수는 동작 후에 return을 통해 결과값을 전달함

- 함수는 함수명()으로 호출
  - parameter가 있는 경우, 함수명(값1, 값2, ...)로 호출

![image-20220129214958134](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129214958134.png)

---

## 함수의 결과값(Output)

### 값에 따른 함수의 종류

- Void function
  - 명시적인 return 값이 없는 경우, None을 반환하고 종료
- Value returning function
  - 함수 실행 후, return문을 통해 값 반환
  - return을 하게 되면, 값 반환 후 함수가 바로 종료

![image-20220129215212089](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129215212089.png)

---

### 두 개 이상의 값 반환

- 아래 코드의 문제점은 무엇일까?

![image-20220129215300593](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129215300593.png)

---

### 튜플 반환

- 반환 값으로 튜플 사용

![image-20220129215354779](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129215354779.png)

---

### 값 반환 외 return문의 용도

- 함수 빠져나가기
  - return을 하게 되면, 값 반환 후 함수가 바로 종료
  - 함수를 빠져나갈 때, return문을 사용

![image-20220129215504513](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129215504513.png)

---

## 함수의 입력(Input)

### Parameter와 Argument

- Parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
- Argument : 함수를 호출 할 때, 넣어주는 값

![image-20220129215700563](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129215700563.png)

---

- Argument(argument)란?
  - 함수 호출 시 함수의  parameter를 통해 전달되는 값
  - Argument는 소괄호 안에 할당 func_name(argument)
    - 필수 Argument : 반드시 전달되어야 하는 argument
    - 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본 값이 전달

---

- Positional Arguments
  - 기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨

![image-20220129220013636](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129220013636.png)

- Keyword Arguments
  - 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
  - Keyword Argument  다음에 Positional Argument를 활용할 수 없음

![image-20220129220116878](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129220116878.png)

- Default Arguments Values
  - 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
    - 정의된 것 보다 더 적은 개수의 argument들로 호출 될 수 있음

![image-20220129220240333](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129220240333.png)

- Positional Arguments **Packing/Unpacking**
  - Positional Arguments Packing/Unpacking 연산자(*)
    - 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
- 언제 사용하는가?
  - 몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용

![image-20220129220435744](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129220435744.png)

- Keyword Arguments Packing/Unpacking 연산자(**)
  - 함수가 임의의 개수 Argument를 Keyword Argument로 호출될 수 있도록 지정
  - Argument들은 딕션너리로 묶여 처리되며, parameter에 **를 붙여 표현

![image-20220129220757652](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129220757652.png)

---

### 함수의 범위(Scope)

- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
- scope
  - global scope : 코드 어디에서든 참조할 수 있는 공간
  - local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능
- variable
  - global variable : global scope에 정의된 변수
  - local variable : local scope에 정의된 변수



### 변수 수명주기(lifecycle)

- 변수는 각자의 수명주기(lifecycle)가 존재

  - built-in scope
    - 파이썬이 실행된 이후부터 영원히 유지

  - global scope
    - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
  - local scope
    - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지



### 이름 검색 규칙(Name Resoultion)

- 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule
  - Local scope : 함수
  - Enclosed scope : 특정 함수의 상위 함수
  - Global scope : 함수 밖의 변수, Import 모듈
  - Built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성

- #### 즉, 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음

---

![image-20220129222311675](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129222311675.png)

---

### 함수의 문서화(Doc-String)

#### Docstring(Document String)

- 함수나 클래스의 설명

![image-20220129223351197](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129223351197.png)

---

### Naming Convention

- 좋은 함수와 parameter 이름을 짓는 방법
  - 상수 이름은 영문 전체를 대문자
  - 클래스 및 예외의 이름은 각 단어의 첫 글자만 영문 대문자
  - 이외 나머지는 소문자 또는 밑줄로 구분한 소문자 사용 -> **함수**

- 스스로를 설명
  - 함수의 이름만으로 어떠한 역할을 하는 함수인지 파악 가능해야 함
  - 어떤 기능을 수행하는지, 결과 값으로 무엇을 반환하는지 등
- 약어 사용을 지양
  - 보편적으로 사용하는 약어를 제외하고 가급적 약어 사용을 지양

---

### 함수 응용

#### 내장 함수(Built-in Functions)

- 파이썬 인터프이터에는 항상 사용할 수 있는 많은 함수와 형(type)이 내장되어 있음

![image-20220129223814604](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129223814604.png)

---

- map(function, iterable)

![image-20220129223908646](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129223908646.png)

![image-20220129223930231](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129223930231.png)

---

- filter(function, iterable)

![image-20220129224016519](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129224016519.png)

---

- zip(*iterables)

![image-20220129224049429](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129224049429.png)

---

- lambda [parameter] : 표현식

  - 람다함수
    - 표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불림
  - 특징
    - return문을 가질 수 없음
    - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
  - 장점
    - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
    - def를 사용 할 수 없는 곳에서도 사용가능

  ```python
  # 삼각형의 넓이를 구하는 공식 - def
  def triangle_area(b, h):
      return 0.5 * b * h
  triangle_area(5, 6)
  # => 15.0
  ```

  ```python
  # 삼각형의 넓이를 구하는 공식 - 람다
  triangle_area = lambda b, h : 0.5 * b * h
  triangle_area(5, 6)
  # => 15.0
  ```

  ---

### 재귀 함수(recursive function)

- 자기 자신을 호출하는 함수
- 무한한 호출을 목표로 하는 것이 아니며, 알고리즘 설계 및 구현에서 유용하게 활용
  - 알고리즘 중 재귀 함수로 로직을 표현하기 쉬운 경우가 있음(예 - 점화식)
  - 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성

![image-20220129225005274](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129225005274.png)

- 재귀 함수 주의 사항
  - 재귀 함수는 base case에 도달할 때까지 함수를 호출함
  - 메모리 스택이 넘치게 되면(stack overflow) 프로그램이 동작하지 않게 됨
  - 파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1,000번으로, 호출 횟수가 이를 넘어가게 되면 Recursion Error 발생


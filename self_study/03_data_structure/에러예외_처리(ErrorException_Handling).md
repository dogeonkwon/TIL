# 에러/예외 처리(Error/Exception Handling)

## 개요

- 디버깅
- 에러와 예외
- 예외 처리
- 예외 발생 시키지



## 디버깅

- "코드의 상태를 신중하게 출력해가며 심사숙고하는 것보다 효과적인 디버깅 도구는 없습니다." - 브라이언 커니핸, Unix for Beginners-
- print 문 활용
  - 특정 함수 결과, 반복 / 조건 결과 등 나눠서 생각
- 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
  - breakpoint, 변수 조회 등
- Python tutor 활용 (단순 파이썬 코드인 경우)
- 뇌컴파일, 눈디버깅
- 코드를 작성하다가...
  - 에러 메시지가 발생하는 경우
    - 해당 하는 위치를 찾아 메시지를 해결
  - 로직 에러가 발생하는 경우
    - 명시적인 에러 메시지 없이 예상과 다른 결과가 나온 경우
      - 정상적으로 동작하였던 코드 이후 작성된 코드를 생각해봄
      - 전체 코드를 살펴봄
      - 휴식을 가져봄
      - 누군가에게 설명해봄

## 에러와 예외

- SyntaxError가 발생하면, 파이썬 프로그램은 실행이 되지 않음
- 파일이름, 줄번호, ^ 문자를 통해 파이썬이 코드를 읽어 나갈 때(parser) 문제가 발생한 위치를 표현
- 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호(^)를 표시

![image-20220130134823996](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130134823996.png)

---

### 문법 에러(Syntax Error)

- Invalid syntax
- assign to literal

![image-20220125092835059](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220125092835059.png)

---

- EOL (End of Line)
- EOF (End of File)

![image-20220125092908946](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220125092908946.png)

---

### 예외(Exception)

- 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
  - 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
- 실행 중에 감지되는 에러들을 예외(Exception)라고 부름
- 예외는 여러 타입(type)으로 나타나고, 타입이 메시지의 일부로 출려됨
  - NameError, TypeError 등은 발생한 예외 타입의 종류(이름)

- 모든 내장 예외는 Exception Class를 상속받아 이뤄짐

- 사용자 정의 예외를 만들어 관리할 수 있음

---

- ZeroDivisionError 
- NameError

![image-20220125095846372](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220125095846372.png)

---

- TypeError - 타입 불일치

![image-20220125095907327](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220125095907327.png)

---

- TypeError - argument 누락

![image-20220125095934792](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220125095934792.png)

---

- TypeError - argument type 불일치

![image-20220130135726179](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130135726179.png)

---

- ValueError - 타입은 올바르나 값이 적절하지 않거나 없는 경우

![image-20220130135747829](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130135747829.png)

---

- IndexError - 인덱스가 존재하지 않거나 범위를 벗어나는 경우

![image-20220130135806597](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130135806597.png)

---

- KeyError - 해당 키가 존재하지 않는 경우

![image-20220130135817022](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130135817022.png)

---

- ModuleNotFoundError - 존재하지 않는 모듈을 import 하는 경우

![image-20220130135848400](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130135848400.png)

---

- ImportError - Module은 있으나 존재하지 않는 클래스/함수를 가져오는 경우

![image-20220130135921700](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130135921700.png)

---

- KeyboardInterrupt - 임의로 프로그램을 종료하였을 때

![image-20220130140001766](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130140001766.png)

---

- IndentationError - Indentation이 적절하지 않는 경우

![image-20220130140036569](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130140036569.png)

---

#### 파이썬 내장 예외(built-in-exceptions)

- 파이썬 내장 예외의 클래스 계층 구조
  - https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy

![image-20220130140207461](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130140207461.png)

---

### 예외처리

- try 문(statement) / except 절(clause)을 이용하여 예외 처리를 할 수 있음
- try 문
  - 오류가 발생할 가능성이 있는 코드를 실행
  - 예외가 발생되지 않으면, except 없이 실행 종료
- except 문
  - 예외가 발생하면, except 절이 실행
  - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함
- else
  - try 문에서 예외가 발생하지 않으면 실행함
- finally
  - 예외 발생 여부와 관계업이 항상 실행함



- 예시

![image-20220130140423697](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130140423697.png)



![image-20220130140536023](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130140536023.png)



- 처리순서

![image-20220130140440420](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130140440420.png)

---

### 예외 처리 종합 예시

- 파일을 열고 읽는 코드를 작성하는 경우
  - 파일 열기 시도
    - 파일 없는 경우 => '해당 파일이 없습니다.' 출력 (except)
    - 파일 있는 경우 => 파일 내용을 출력 (else)
  - 해당 파일 읽기 작업 종료 메시지 출력 (finally)

![image-20220130144354869](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130144354869.png)



![image-20220130144417442](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130144417442.png)

## 예외 발생 시키기

### raise statement

- raise를 통해 예외를 강제로 발생

![image-20220130144604574](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130144604574.png)



![image-20220130144616558](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130144616558.png)



### assert statement

- assert를 통해 예외를 강제로 발생
- assert는 상태를 검증하는데 사용되며, 무조건 AssertionError가 발생
- 일반적으로 디버깅 용도로 사용

![image-20220130144747439](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130144747439.png)



![image-20220130144823238](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130144823238.png)



![image-20220130145110308](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130145110308.png)


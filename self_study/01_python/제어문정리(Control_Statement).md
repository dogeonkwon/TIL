# 제어문(Control Statement)



- ## 제어문

  - 조건문
  - 반복문



### 제어문(Control Statement)

- 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행
- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요함
- 제어문은 순서도(flow chart)로 표현이 가능



### 조건문(Condistional Statement)

- #### 조건문 기본

  - 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용

![image-20220129205648035](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129205648035.png)

- exprsssion에는 참/거짓에 대한 조건식
  - 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블럭을 실행
  - 이외의 경우 else 이후 들여쓰기 되어있는 코드 블럭을 실행
    - else는 선택적으로 활용 가능함

![image-20220129205814735](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129205814735.png)

---

![image-20220129205847093](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129205847093.png)

---

- 조건문을 통해 변수 num의 값으 홀수/짝수 여부를 출력하시오.
  - 이때 num은 input을 통해 사용자로부터 입력을 받으시오.

```python
num = int(input('숫자 입력: '))
if num % 2:   # if num % 2 == 1:
    print('홀수입니다.')
else:
    print('짝수입니다.')
```



### 복수 조건문

- 복수의 조건식을 활용할 경우 elif를 활용하여 표현함

![image-20220129210510461](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129210510461.png)

---

### 중첩 조건문

- 조건문은 다른 조건문에 중첩되어 사용될 수 있음
  - 들여쓰기를 유의하여 작성할 것

- 실습 문제
  - 아래의 코드에서 중첩조건문을 활용하여 미세먼지 농도(dust 값)이 300이 넘는 경우 '실외 활동을 자제하세요'를 추가적으로 출력하고 음수인 경우 '값이 잘 못 되었습니다'를 출력하시오.

![image-20220129210909763](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129210909763.png)

---

### 조건 표현식

- 조건표현식(Conditional Expression)이란?
  - 조건 표현식을 일반적으로 조건에 따라 값을 정할 때 활용
  - 삼항 연산자(Ternary Operator)로 부르기도 함

![image-20220129211058877](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129211058877.png)

---

### 반복문(Loop Statement)

- 특정 조건을 도달할 때까지, 계속 반복되는 일련의 문장

![image-20220129211238300](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129211238300.png)

---

- while 문
  - 종료조건에 해당하는 코드를 통해 반복문을 종료시켜야 함
- for 문
  - 반복가능한 객체를 모두 순회하면 종료(별도의 종료조건이 필요 없음)
- 반복 제어
  - break, continue, for-else

---

### While문

- while문은 조건식이 참인 경우 반복적으로 코드를 실행
  - 조건이 참인 경우 들여쓰기 되어 있는 코드 블록이 실행됨
  - 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨
  - while문은 무한 루프를 하지 않도록 종료조건이 반드시 필요

![image-20220129211618758](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129211618758.png)

---

### For문

- For문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)요소를 모두 순회함
  - 처음부터 끝까지 모두 순회하므로 별도의 종료조건이 필요하지 않음

![image-20220129211812492](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129211812492.png)

---

- Iterable
  - 순회할 수 있는 자료형(str, list, dict 등)
  - 순회형 함수(range, enumerate)

![image-20220129212042377](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129212042377.png)

---

- 문자열(String) 순회
  - 사용자가 입력한 문자를 한 글자씩 출력하시오.

![image-20220129212144777](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129212144777.png)

---

![image-20220129212210417](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129212210417.png)

---

- 딕셔너리(Dictionary) 순회
  - 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용

![image-20220129212301585](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129212301585.png)

---

- 추가 메서드를 활용하여 순회할 수 있음
  - key() : Key로 구성된 결과
  - values() : Value로 구성된 결과
  - items() : (Key, Value)의 튜플로 구성된 결과

![image-20220129212432445](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129212432445.png)

![image-20220129212609007](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129212609007.png)

---

- enumerate()
  - 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
    - (index, value) 형태의 tuple로 구성된 열거 객체를 반환

![image-20220129212659232](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129212659232.png)

---

- List Comprehension
  - 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

![image-20220129212800591](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129212800591.png)

---

![image-20220129213018717](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129213018717.png)

---

![image-20220129213038954](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129213038954.png)

---

### 반복문 제어

- break
  - 반복문을 종료
- continue
  - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
- for-else
  - 끝까지 반복문을 실행한 이후에 else문 실행
    - break를 통해 중간에 종료되는 경우 else 문은 실행되지 않음

---

- break
  - break문을 만나면 반복문은 종료됨

![image-20220129213307643](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129213307643.png)



---

- continue
  - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

![image-20220129213426226](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129213426226.png)

---

- pass
  -  아무것도 하지 않음
    - 특별히 할 일이 없을 때 자리를 채우는 용도로 상용
    - 반복문 아니여도 사용 가능

![image-20220129213519769](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129213519769.png)

---

- else
  - 끝까지 반복문을 실행한 이후에 else문 실행

![image-20220129213615076](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129213615076.png)

---

- 반복문 제어 정리

![image-20220129213658021](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129213658021.png)
# 데이터 구조(Data Structure)



- ## 순서가 ***있는***  데이터 구조

  - #### 문자열(String) - immutable(불변)

  - #### 리스트(List) - mutable(가변)

  - #### 튜플(Tuple) - immutable(불변)



- ## 순서가 ***없는***  데이터 구조

  - #### 셋(Set) - mutable(가변)

  - #### 딕셔너리(Dictionary) - mutable(가변)





## 순서가 있는 데이터 구조

### 문자열(String Type)

- 문자들의 나열(sequence of characters)
  - 모든 문자는 str 타입
- 문자열은 작은 따옴표(')나 큰 따옴표(")를 활용하여 표기
  - 문자열을 묶을 때 동일한 문장부호를 활용
  - PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함

![image-20220129154651290](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129154651290.png)



- ##### 문자열 조회/탐색 및 검증 메소드

| 문법          | 설명                                                         |
| ------------- | ------------------------------------------------------------ |
| s.find(x)     | x의 첫 번째 위치를 반환. 없으면, -1을 반환                   |
| s.index(x)    | x의 첫 번째 위치를 반환. 없으면, 오류 방생                   |
| s.isalpha()   | 알파벳 문자 여부<br />*단순 알파벳이 아닌 유니코드 상 Letter (한국어도 포함) |
| s.isupper()   | 대문자 여부                                                  |
| s.islower()   | 소문자 여부                                                  |
| s.istitle()   | 타이틀 형식 여부                                             |
| s.isdigit()   | 해당 문자열이 '숫자'로 이루어져 있는지 검사한다.             |
| s.idecimal()  | 해당 문자열이 0~9까지의 수로 이루어진 것인지 검사한다. <br />다시 말해, int로 바로 변환할 수 있는 수인지를 검사한다. |
| s.isnumeric() | 이 함수를 '수로 볼 수 있는 것'인 경우 True를 반환한다.       |

```python
x = '3²'
x.isdigit()
# True
x.isdecimal()
# False
int(x)
# ERROR!!!!
```



- ##### 문자열 변경 메소드

| 문법                         | 설명                                       |
| ---------------------------- | ------------------------------------------ |
| s.replace(old, new[,count])  | 바꿀 대상 글자를 새로운 글자로 바꿔서 반환 |
| s.strip([chars])             | 공백이나 특정 문자를 제거                  |
| s.split([chars])             | 공백이나 특정 문자를 기준으로 분리         |
| 'separator'.join([iterable]) | 구분자로 iterable을 합침                   |
| s.capitalize()               | 가장 첫 번째 글자를 대문자로               |
| s.title()                    | `'`나 공백 이후를 대문자로                 |
| s.upper()                    | 모두 대문자                                |
| s.lower()                    | 모두 소문자                                |
| s.swapcase()                 | 대 <->소문자 변경하여                      |

- s.replace(old, new[,count])

![image-20220129160417860](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129160417860.png)



- s.strip([chars])

![image-20220129160506156](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129160506156.png)



- s.split([chars])

![image-20220129160530204](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129160530204.png)

- 'separator'.join([iterable])

![image-20220129160557663](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129160557663.png)



### 리스트(List)

- 순서를 가지는 0개 이상의 객체를 참조하는 자료형
  - 생성된 이후 내용 변경이 가능 -> 가변자료형
  - 유연성 때문에 파이썬에서 가장 흔히 사용
- 항상 대괄호 형태로 출력



| 문법                   | 설명                                                         |
| ---------------------- | ------------------------------------------------------------ |
| L.append(x)            | 리스트 마지막에 항목 x를 추가                                |
| L.insert(i, x)         | 리스트 인덱스 i에 항목 x를 삽입                              |
| L.remove(x)            | 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거<br />항목이 존재하지 않을 경우, ValueError |
| L.pop()                | 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거        |
| L.pop(i)               | 리스트의 인덱스 i에 있는 항목을 반환 후 제거                 |
| L.extend(m)            | 순회형 m의 모든 항목들의 리스트 끝에 추가 (+=과 같은 기능)   |
| L.index(x, start, end) | 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환 |
| L.reverse()            | 리스트를 거꾸로 정렬                                         |
| L.sort(...)            | 리스트를 정령 (매개변수 이용가능)                            |
| L.count(x)             | 리스트에서 항목 x가 몇 개 존재하는지 갯수를 반환             |
| L.clear()              | 모든 항목을 삭제함                                           |

---

- L.append(x)

![image-20220129161224185](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129161224185.png)

---

- L.insert(i, x)

![image-20220129161303402](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129161303402.png)

---

- L.remove(x)  

![image-20220129161314686](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129161314686.png)

---

- L.pop(i)

![image-20220129161334300](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129161334300.png)

--------

- L.extend(m)  

![image-20220129161524047](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129161524047.png)

----

- L.index(x, start, end)

![image-20220129161656642](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129161656642.png)

---

-  L.reverse() 

![image-20220129161733689](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129161733689.png)

---

- L.sort(...)

![image-20220129161820426](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129161820426.png)

---

- L.count(x)  

![image-20220129161901241](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129161901241.png)

---

- L.clear()

![image-20220129161950173](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129161950173.png)

---

### 튜플(Tuple)

- 순서를 가지는 0개 이상의 객체를 참조하는 자료형
  - 생성 후, 담고있는 객체 변경이 불가 -> **불변 자료형(immutable)**
- 항상 소괄호 형태로 출력

- 튜플은 변경할 수 없기 때문에 값에 영향을 미치지 않는 메소드만을 지원
- 리스트 메소드 중 항목을 변경하는 메소드들을 제외하고 대부분 동일

![image-20220129162258724](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129162258724.png)

---



## 순서가 없는 데이터 구조

### 셋(Set)

- 순서없이 0개 이상의 해시가능한 객체를 참조하는 자료형
  - 해시 가능한 객체(불변자료형)만 담을 수 있음
- 담고있는 객체를 삽입 변경, 삭제 가능 -> **가변자료형(mutable)**
- 수학에서의 집합과 동일한 구조를 가짐
  - 중복된 값이 존재하지 않음



- #### 셋 메소드

| 문법           | 설명                                                         |
| -------------- | ------------------------------------------------------------ |
| s.copy()       | 셋의 얕은 복사본을 반환                                      |
| s.add(x)       | 항목 x가 셋 s에 없다면 추가                                  |
| s.pop()        | 셋s에서 랜덤하게 항복을 반환하고, 해당 항목을 제거<br />set이 비어 있을 경우, Key Error |
| s.remove(x)    | 항목 x를 셋 s에서 삭제<br />항목이 존재하지 않을 경우, Key Error |
| s.discard(x)   | 항목 x가 셋 s에 있는 경우, 항목 x를 셋s에서 삭제             |
| s.update(t)    | 셋 t에 있는 모든 항목 중 셋s에 없는 항목을 추가              |
| s.clear()      | 모든 항목을 제거                                             |
| s.isdisjoint() | 셋 s가 셋 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True반환 |
| s.issubset()   | 셋 s가 셋 t의 하위 셋인 경우, True반환                       |
| s.issuperset() | 셋 s가 셋 t의 상위 셋인 경우, True반환                       |

---

- s.add(x)

![image-20220129163103053](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129163103053.png)

---

- s.pop()  

![image-20220129163320278](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129163320278.png)

---

- s.remove(x)  

![image-20220129163243827](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129163243827.png)

---

- s.discard(x)  

![image-20220129163310735](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129163310735.png)

---

- s.update(t)  

![image-20220129163259439](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129163259439.png)

---

### 딕셔너리(Dictionary)

- 순서 없이 키-값(key-value) 쌍으로 이뤄진 객체를 참조하는 자료형
- 딕셔너리의 키(key)
  - 해시가능한 불변 자료형만 가능
- 각 키의 값(values)
  - 어떠한 형태든 관계 없음



- ### 딕셔너리 메소드

| 문법          | 설명                                                         |
| ------------- | ------------------------------------------------------------ |
| d.clear()     | 모든 항목을 제거                                             |
| d.copy()      | 딕셔너리 d의 얕은 복사본을 반환                              |
| d.keys()      | 딕셔너리 d의 모든 키를 담은 뷰를 반환                        |
| d.values()    | 딕셔너리 d의 모든 값을 담은 뷰를 반환                        |
| d.items()     | 딕셔너리 d의 모든 키-값 쌍을 담은 뷰를 반환                  |
| d.get(k)      | 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 None을 반환 |
| d.get(k, v)   | 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 v를 반환 |
| d.pop(k)      | 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데,<br />키 k가 딕셔너리 d에 없을 경우 KeyError를 발생 |
| d.get(k, v)   | 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데,<br />키 k가 딕셔너리 d에 없을 경우 v를 발생 |
| d.update(...) | 딕셔너리 d의 값을 매핑하여 업데이트                          |

---

- d.pop(k)

![image-20220129164311229](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129164311229.png)

![image-20220129164359300](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129164359300.png)

---

- d.get(k, v)

![image-20220129164418073](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129164418073.png)

- dictionary에서 for를 활용하는 4가지 방법

```python
# 1. dictionary 순회(key 활용)
for key in dict:
    print(key)
    print(dict[key])
```



```python
# 2. '.key()' 활용
for key in dict.keys():
    print(val)
```



```python
# 3. '.values()' 활용
for val in dict.values():
    print(val)
```



```python
# 4. '.items()' 활용
for key, val in dict.items():
    print(key, val)
```





---

- d.update(...)

![image-20220129164429846](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129164429846.png)

---



# ***얕은 복사와 깊은 복사(Shallow Copy & Deep Copy)***

#### 복사 방법

- 할당 (Assignment)
  - 대입 연산자 (=)
    - 리스트 복사 확인하기

![image-20220129165614214](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129165614214.png)



![image-20220129165853070](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129165853070.png)

---

- ## 얕은 복사 (Shallow copy)
  
  - Slice 연산자 활용하여 같은 원소를 가진 리스트지만 연산된 결과를 복사 (다른 주소)

![image-20220129165957441](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129165957441.png)



- - 복사하는 리스트의 원소가 주소를 참조한는 경우

![image-20220129170119222](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129170119222.png)

---

- ## 깊은 복사 (Deep copy)
  
  - 리스트 복사 확인하기 

![image-20220129170207238](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220129170207238.png)
# 모듈

### 개요

- 모듈과 패키지
- 파이썬 표준 라이브러리
- 가상환경
- 유용한 패키지와 모듈
- 사용자 모듈과 패키지



## 모듈과 패키지

- 모듈
  - 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
- 패키지
  - 특정 기능과 관련된 여러 모듈의 집합
  - 패키지 않에는 또 다른 서브 패키지를 포함

- 모듈과 패키지 불러오기
  - **import** module
  - **from** module **import** var, function, class
  - **from** module **import** *
  - **from** package **import** module
  - **from** package.module **import** var, function, class

---

## 파이썬 표준 라이브러리

- 파이썬 표준 라이브러리(Python Standard Library, PSL)
  - 파이썬에 기본적으로 설치된 모듈과 내장 함수
    - https://docs.python.org/ko/3/library/index.html

---

- 파이썬 패키지 관리자(pip) 명령어

  - PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템

  - 패키지 설치
    - 최신 버전 / 특정 버전 / 최소 버전을 명시하여 설치 할 수 있음
    - 이미 설치되어 있는 경우 이미 설치되어 있음을 알리고 아무것도 하지 않음

![image-20220130125849407](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130125849407.png)

---

- 패키지 설치
  - 최신 버전 / 특정 버전 / 최소 버전을 명시하여 설치 할 수 있음

![image-20220130130003307](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130130003307.png)

---

- 패키지 삭제
  - pip는 패키지를 업그레이드 하는 경우 과거 버전을 자동으로 지워줌

![image-20220130130058917](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130130058917.png)

---

- 패키지 목록 및 특정 패키지 정보

![image-20220130130128169](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130130128169.png)

---

- 패키지 freeze
  - 설치된 패키지의 비슷한 목록을 만들지만, pip install에서 활용되는 형식으로 출력
  - 해당하는 목록을 requirements.txt(관습)으로 만들어 관리함

![image-20220130131000030](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130131000030.png)

---

- 패키지 관리하기
  - 아래의 명령어들을 통해 패키지 목록을 관리[1]하고 설치할 수 있음[2]
  - 일반적으로 패키지를 기록하는 파일의 이름은 requirements.txt로 정의함

![image-20220130131118425](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130131118425.png)



![image-20220130131148925](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130131148925.png)



![image-20220130131212655](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130131212655.png)

---

### 사용자 모듈과 패키지

- 모듈 만들기 - check
  - check.py에 짝수를 판별하는 함수(even)와 홀수를 판별하는 함수(odd)를 만들고 check 모듈을 활용 해보시오.

![image-20220130131532728](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130131532728.png)



- 모듈을 활용하기 위해서는 import 문을 통해 가져옴

![image-20220130131619214](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130131619214.png)



![image-20220130131641895](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130131641895.png)

---

- 패키지
  - 패키지는 여러 모듈/하위 패키지로 구조화
    - 활용 예시 : package.module
  - 모든 폴더에는 `__init__.py`를 만들어 패키지로 인식
    - Python 3.3부터는 파일이 없어도 되지만, 하위 버전 호환 및 프레임워크 등에서의 동작을 위해 파일을 생성하는 것을 권장

- 패키지 만들기
  - 수학과 통계 기능이 들어간 패키지를 아래와 같이 구성
    - math의 tools : 자연 상수 e, 원주율 pi 값, 최대값을 구하는 my_ max 함수
    - statistics의 tools : 평균을 구하는 mean 함수

![image-20220130132025222](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130132025222.png)

---

## 가상환경

### 가상환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치를 해야함
- 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
  - 과거 외주 프로젝트 - django 버전 2.x
  - 신규 회사 프로젝트 - django 버전 3.x
- 이러한 경우 가상환경을 만들어 프로젝트별로 독립적인 패키지를 관리 할 수 있음

---

### venv

- 가상 환경을 만들고 관리하는데 사용되는 모듈 (Python 버전 3.5부터)
- 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
  - 특정 폴더에 가상 환경이(패키지 집합 폴더 등) 있고
  - 실행 환경(예 - bash)에서 가상환경을 활성화 시켜
  - 해당 폴더에 있는 패키지를 관리 / 사용함

---

### 가상환경 생성 

- 가상환경을 생성하면, 해당 디렉토리에 별도의 파이썬 패키지가 설치됨

![image-20220130132537435](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130132537435.png)

---

- 가상환경 활성화 / 비활성화
  - 아래의 명령어를 통해 가상환경을 활성화
    - <venv>는 가상환경을 포함하는 디렉토리의 경로

![image-20220130132918825](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130132918825.png)

- 가상환경 비활성화는 $ deactivate 명령어를 사용

---

- cmd와 bash 환경

![image-20220130133118013](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130133118013.png)



![image-20220130133135939](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130133135939.png)



![image-20220130133151979](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220130133151979.png)


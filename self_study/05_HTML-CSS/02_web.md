

# Web

- 목차
- CSS Layout
  - float
  - flexbox
  - grid
- bootstrap
  - bootstrap grid system
- Responsive web



---



- ## CSS Layout

- Display
- Position
- Float
- Flexbox
- Grid
- 기타



---



## Float



![image-20220212230631340](Web&CSS_사진모음/image-20220212230631340.png)





![image-20220212230548811](Web&CSS_사진모음/image-20220212230548811.png)



![image-20220212230557565](Web&CSS_사진모음/image-20220212230557565.png)



![image-20220212230649319](Web&CSS_사진모음/image-20220212230649319.png)



![image-20220212230715140](Web&CSS_사진모음/image-20220212230715140.png)



![image-20220212230820710](Web&CSS_사진모음/image-20220212230820710.png)



- ### Clearing Float

  - Float는 Normal Flow에서 벗어나 부동 상태(떠 있음)
  - 따라서, 이후 요소에 대하여 Float 속성이 적용되지 않도록 Clearing이 필수적임
    - ::after : 선택한 요소의 맨 마지막 자식으로 가상 요소를 하나 생성
      - 보통 content 속성과 함께 짝지어, 요소에 장식용 콘텐츠를 추가할 때 사용
    - clear 속성 부여

```css
.clearfix::after {
	content: "";
    display: block;
    clear: both;
}
```



- Float는 최근에 Flexbox, Grid 등장과 함께 사용도가 낮아짐
- Float 활용 전략 - Normal Flow 에서 벗어난 레이아웃 구성
  - 원하는 요소들을 Float로 지정하여 배치
  - 부모 요소에 반드시 Clearing Float를 하여 이후 요소부터 Normal Flow를 가지도록 지정



---



## Flexbox

- ### CSS Flexible Box Layout

  - 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
  - 축
    - main axis (메인 축)
    - cross axis (교차 축)
  - 구성 요소
    - Flex Container (부모 요소)
    - Flex Item (자식 요소)

![image-20220212231602102](Web&CSS_사진모음/image-20220212231602102.png)



---



- ### Flexbox 구성 요소

  - Flex Container (부모 요소)
    - flexbox 레이아웃을 형성하는 가장 기본적인 모델
    - Flex Item 들이 놓여있는 영역
    - display 속성을 flex 혹은 inline-flex 로 지정
  - Flex Item (자식 요소)
    - 컨테이너에 속해 있는 컨텐츠 (박스)

![image-20220212231811201](Web&CSS_사진모음/image-20220212231811201.png)



- 그렇다면 왜 Flexbox를 사용해야 할까?
  - 이전까지 Normal Flow를 벗어나느 수단은 Float 혹은 Position 이었고 
  - (수동 값 부여 없이) 1. 수직정렬
  - 2. 아이템의 너비와 높이 혹은 간격을 동일하게 배치
- Flexbox가 이를 해결해줌



---



- ### Flex 속성

- 배치 설정

  - flex-direction
  - flex-wrap

- 공간 나누기

  - justify-content (main axis)
  - align-content (cross axis)

- 정렬

  - align-items (모든 아이템을 cross axis 기준으로)
  - align-self (개별 아이템)

---

- #### flex-direction

  - Main axis 기준 방향 설정
  - 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의 (웹 접근성에 영향)



![image-20220212232208933](Web&CSS_사진모음/image-20220212232208933.png)

---

- #### flex-wrap

  - 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
  - 즉, 기본적인 컨텐이너 영역을 벗어나지 않도록 함
  - flex-wrap : 요소들이 강제로 한 줄에 배치 되게 할 것인지 여부 설정
    - wrap : 넘치면 그 다음 줄로 배치
    - nowrap (기본 값) : 한 줄에 배치

![image-20220212232258116](Web&CSS_사진모음/image-20220212232258116.png)

---

- #### flex-direction & flex-wrap

  - flex-direction : Main axis의 방향을 설정
  - flex-wrap : 요소들이 강제로 한 줄에 배치 되게 할 것인지 여부 설정
  - flex-flow
    - flex-direction 과 flex-wrap 의 shorthand
    - flex-direction 과 flex-wrap 에 대한 설정 값을 차례로 작성
    - ex ) flex-flow: row nowrap;

---

- #### justify-content

  - Main axis를 기준으로 공간 배분

![image-20220212232647414](Web&CSS_사진모음/image-20220212232647414.png)

---

- align-content
  - Cross axis를 기준으로 공간 배분 (아이템이 한 줄로 배치되는 경우 확인할 수 없음)

![image-20220212232744579](Web&CSS_사진모음/image-20220212232744579.png)

---

- #### justify-content & align-content

  - 공간 배분
    - flex-start (기본 값) : 아이템들을 axis 시작점으로
    - flex-end : 아이템들을 axis 끝 쪽으로
    - center : 아이템들을 axis 중앙으로
    - space-between : 아이템 사이의 간격을 균일하게 분배
    - space-around : 아이템을 둘러싼 영역을 균일하게 분배 (가질 수 있는 영역을 반으로 나눠서 양쪽에)
    - space-evenly : 전체 영역에서 아이템 간 간격을 균일하게 분배

---

- #### align-items

  - 모든 아이템을 Cross axis를 기준으로 정렬

![image-20220212233149885](Web&CSS_사진모음/image-20220212233149885.png)

---

- #### align-self

  - 개별 아이템을 Cross axis 기준으로 정렬
    - <span style="color:red">주의! 해당 속성은 컨테이너에 적용하는 것이 아니라 개별 아이템에 적용</span>

![image-20220212233302039](Web&CSS_사진모음/image-20220212233302039.png)

---

- #### align-items & align-self

  - Cross axis를 중심으로
    - stretch(기본 값) : 컨테이너를 가득 채움
    - flex-start : 위
    - flex-end : 아래
    - center : 가운데
    - baseline : 텍스트 baseline에 기준선을 맞춤

---

- 기타 속성

![image-20220212233447185](Web&CSS_사진모음/image-20220212233447185.png)



![image-20220212233509648](Web&CSS_사진모음/image-20220212233509648.png)



---



## Bootstrap

![image-20220212233535736](Web&CSS_사진모음/image-20220212233535736.png)



![image-20220212233556359](Web&CSS_사진모음/image-20220212233556359.png)



---



- 더 편하게 상요해보자(CDN)

![image-20220212233643598](Web&CSS_사진모음/image-20220212233643598.png)

![image-20220212233618969](Web&CSS_사진모음/image-20220212233618969.png)



---



- ### spacing

![image-20220212233924295](Web&CSS_사진모음/image-20220212233924295.png)

![image-20220212233939348](Web&CSS_사진모음/image-20220212233939348.png)



| class name | rem  |  px  |
| :--------: | :--: | :--: |
|    m-1     | 0.25 |  4   |
|    m-2     | 0.5  |  8   |
|    m-3     |  1   |  16  |
|    m-4     | 1.5  |  24  |
|    m-5     |  3   |  48  |



![image-20220212233954998](Web&CSS_사진모음/image-20220212233954998.png)



- #### .mx-auto (수평 중앙 정렬)

![image-20220212234010913](Web&CSS_사진모음/image-20220212234010913.png)

- ### spacing 종합

- m, p / t, b, s, e, x, y / 0, 1, 2, 3, 4, 5

![image-20220212234042798](Web&CSS_사진모음/image-20220212234042798.png)



---



- ### color

![image-20220212234154309](Web&CSS_사진모음/image-20220212234154309.png)



---

- ### Text

![image-20220212234224348](Web&CSS_사진모음/image-20220212234224348.png)



---



- ### display

![image-20220212234259767](Web&CSS_사진모음/image-20220212234259767.png)



---



- ### Responsive Web Design

  - 반응형 웹은 별도의 기술 이름이 아닌 웹 디자인에 대한 접근 방식, 반응형 레이아웃 작성에 도움이 되는 사례들의 모음 등을 기술하는데 사용되는 용어
  - ex ) Media Queries, Flexbox, Bootstrap, Grid System 등



---



## Bootstrap Grid System

- ### Grid system (web design)

  - 요소들의 디자인과 배치에 도움을 주는 시스템
  - 기본요소
    - Column : 실제 컨텐츠를 포함하는 부분
    - Gutter : 칼럼과 칼럼 사이의 공간 (사이 간격)
    - Container : Column 들을 담고 있는 공간

![image-20220212234703939](Web&CSS_사진모음/image-20220212234703939.png)



- ##### Bootstrap Grid System은 flexbox로 제작됨

- ##### container, rows, column으로 컨텐츠를 배치하고 정렬

- #### <span style="color:red">반드시 기억해야 할 2가지 !</span>

  - ##### 12개의 column

  - ##### 6개의 grid breakpoints



- 일단 사용해보면...

![image-20220212234908227](Web&CSS_사진모음/image-20220212234908227.png)



![image-20220212234949280](Web&CSS_사진모음/image-20220212234949280.png)

- ##### Grid System breakpoints

![image-20220212235024743](Web&CSS_사진모음/image-20220212235024743.png)

|                      |     xs      |    sm    |    md    |    lg    |    xl     |    xxl    |
| :------------------: | :---------: | :------: | :------: | :------: | :-------: | :-------: |
|                      |   < 576px   | >= 576px | >= 768px | >= 992px | >= 1200px | >= 1400px |
| container(max-width) | None (auto) |  540px   |  720px   |  960px   |  1140px   |  1320px   |
|     Class prefix     |    .col-    | .col-sm- | .col-md- | .col-lg- | .col-xl-  | .col-xxl- |



---



![image-20220212235408624](Web&CSS_사진모음/image-20220212235408624.png)

![image-20220212235347388](Web&CSS_사진모음/image-20220212235347388.png)



---



![image-20220212235438676](Web&CSS_사진모음/image-20220212235438676.png)

![image-20220212235448824](Web&CSS_사진모음/image-20220212235448824.png)



---



![image-20220212235504133](Web&CSS_사진모음/image-20220212235504133.png)

![image-20220212235513743](Web&CSS_사진모음/image-20220212235513743.png)



---



![image-20220212235549220](Web&CSS_사진모음/image-20220212235549220.png)

![image-20220212235600460](Web&CSS_사진모음/image-20220212235600460.png)



---



![image-20220212235615888](Web&CSS_사진모음/image-20220212235615888.png)

![image-20220212235625348](Web&CSS_사진모음/image-20220212235625348.png)



---



![image-20220212235639043](Web&CSS_사진모음/image-20220212235639043.png)

![image-20220212235647969](Web&CSS_사진모음/image-20220212235647969.png)

---

- ##### @media 활용

![image-20220212235724298](Web&CSS_사진모음/image-20220212235724298.png)

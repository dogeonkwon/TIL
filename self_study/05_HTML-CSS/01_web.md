# HTML



- ## HTML

  - #### HTML 기본구조

  - #### HTML 문서 구조화



## HTML(Hyper Text Markup Language)



[WHATWG](https://whatwg.org/) 표준을 알기 위해서는 이 사이트 많이 사용할 예정 - ***즐겨찾기 눌러놓기!***

- 이걸 기준으로 개발을 많이 하고 있음



모든 언어의 공식문서

[mdn](https://developer.mozilla.org/ko/) - 파이썬 뿐만 아니라 자바 등등 모든 언어들의 공식문서

그 중에서

[html mdn](https://developer.mozilla.org/ko/docs/Web/HTML) 이 사이트는 특별히 html 공식문서 ***즐겨찾기 눌러놓기!***

[w3school](https://www.w3schools.com/) html을 어떻게 사용하는지 , 어떻게 쓰는 거였더라 헷갈릴 때 사용! ***즐겨찾기 눌러놓기!***



## HTML 기본 구조

- #### html : 문서의 최상위(root)요소

- #### head : 문서 메타데이터 요소

  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용

- #### body : 문서 본문 요소

  - 실제 화면 구성과 관련된 내용



![image-20220205220801960](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205220801960.png)

---

- ### head 예시

  - `<title>` : 브라우저 상단 타이틀
  - `<meta>` : 문서 레벨 메타데이터 요소
  - `<link>` : 외부 리소스 연결 요소 (CSS 파일, favicon 등)
  - `<script>` : 스크립트 요소 (JavaScript 파일/코드)
  - `<style>` : CSS 직접 작성

![image-20220205221033994](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205221033994.png)

---

- ### DOM(Document Object Model) 트리

  - 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
    - HTML 문서에 대한 모델을 구성함
    - HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공함

![image-20220205221251031](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205221251031.png)



![image-20220205221302167](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205221302167.png)

---

- ### 요소(element)

  - `<h1>`contents`</h1>`
    - html의 요소는 태그와 내용(contents)로 구성되어 있다.

![image-20220205221432850](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205221432850.png)



- HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
  - 태그(Element, 요소)는 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
- 내용이 없는 태그들
  - br, hr, img, input, link, meta
- 요소는 중첩(nested)될 수 있음
  - 요소의 중첩을 통해 하나의 문서를 구조화
  - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
    - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어 질 수 있음

---

- ### 속성(attribute)

  - `<a href="https://google.com"></a>`
    - 태그별로 사용할 수 있는 속성은 다르다.
    - 공백은 no!, 쌍따옴표 사용!

![image-20220205221825914](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205221825914.png)





![image-20220205221846852](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205221846852.png)

- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있음

---

- ### HTML Global Attribute

  - 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성
    - id : 문서 전체에서 유일한 고유 식별자 지정
    - class : 공백으로 구분된 해당 요소의 클래스의 목록 (css, js에서 요소를 선택하거나 접근)
    - data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
    - style : inline 스타일
    - title : 요소에 대한 추가 정보 지정
    - tabindex : 요소의 탭 순서

![image-20220205222325903](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205222325903.png)

---

- ### 시맨틱 태그

  - HTML5에서 의미론적 요소를 담은 태그의 등장
    - 기존 영역을 의미하는 div 태그를 대체하여 사용
  - 대표적인 태그 목록
    - header : 문서 전체나 섹션의 헤더(머리말 부분)
    - nav : 내비게이션
    - aside : 사이드에 위치한 공간, 메인 컨텐츠와 관련성이 적은 콘텐츠
    - section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
    - article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
    - footer : 문서 전체나 섹션의 푸터(마지막 부분)

  ![image-20220205222556206](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205222556206.png)

---

## HTML 문서 구조화

- ### 텍스트 요소

| 태그                               | 설명                                                         |
| ---------------------------------- | ------------------------------------------------------------ |
| `<a></a>`                          | href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성     |
| `<b></b>`<br />`<strong></strong>` | 굵은 글씨 요소<br />강조하고자 하는 요소 (보통 굵은 글씨로 표현) |
| `<i></i>`<br>`<em></em>`           | 기울임 글씨 요소<br />강조하고자 하는 요소 (보통 기울임 글씨로 표현) |
| `<br>`                             | 텍스트 내에 줄 바꿈 생성                                     |
| `<img>`                            | src 속성을 활용하여 이미지 표현                              |
| `<span></span>`                    | 의미 없는 인라인 컨테이너                                    |

![image-20220205223138551](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205223138551.png)

---

- ### 그룹 컨텐츠

| 태그                         | 설명                                                         |
| ---------------------------- | ------------------------------------------------------------ |
| `<p></p>`                    | 하나의 문단                                                  |
| `<hr>`                       | 문단 레벨 요소에서의 주제의 분리를 의미하며 수평선으로 표현됨 |
| `<ol></ol>`<br />`<ul></ul>` | 순서가 있는 리스트(ordered)<br />순서가 없는 리스트(unordered) |
| `<pre></pre>`                | HTML에 작성한 내용을 그대로 표현.<br />보통 고정폭 글꼴이 사용되고 공백문자를 유지 |
| `<blockquote></blockquote>`  | 텍스트가 긴 인용문, 주로 들여쓰기를 한 것으로 표현           |
| `<div></div>`                | 의미 없는 블록 레벨 컨테이너                                 |

![image-20220205223459897](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205223459897.png)

---

- ### Table

  - table의 각 영역을 명시하기 위해 `<thead>` `<tbody>` `<tfoot>` 요소를 활용

![image-20220205223608181](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205223608181.png)

- `<tr>` 으로 가로 줄을 구성하고 내부에는 `<th>` 혹은 `<td>` 로 셀을 구성

![image-20220205223708766](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205223708766.png)

- `colspan`, `rowspan` 속석을 활용하여 셀 병합

![image-20220205223745399](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205223745399.png)

- `<caption>` 을 통해 표 설명 또는 제목을 나타냄

![image-20220205223818533](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205223818533.png)

---

- ### vscode에서 직접 해보기

  - table 태그 기본 구성
    - thead
      - tr > th
    - tbody
      - tr > td
    - tfoot
      - tr > td
    - caption

![image-20220205223949171](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205223949171.png)

---

- ### form

  - `<form>` 은 정보(데이터)를 서버에 제출하기 위한 영역
  - `<form>` 기본 속성
    - action : form을 처리할 서버의 URL
    - method : form을 제출할 때 사용할 HTTP 메서드
    - enctype : method가 post인 경우 데이터의 유형
      - application/x-www-form-urlencoded : 기본값
      - multipart/form-data : 파일 전송시 (input type이 file인 경우)

![image-20220205224230934](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205224230934.png)

---

- ### input

  - 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공
  - `<input>` 대표적인 속성
    - name : form control에 적용되는 이름
    - value : form control에 적용되는 값
    - required, readonly, autofocus, autocomplete, disabled 등

![image-20220205224508765](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205224508765.png)

---

- ### input label

  - label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
    - 사용자는 선택할 수 있는 영역이 늘어나 웹 / 모바일 환경에서 편하게 사용할 수 있음
    - label과 input 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어 쉽게 내용을 확인 할 수 있도록 함
  - `<input>`에 id 속성을, `<label>`에는 for 속성을 활용하여 상호 연관을 시킴

![image-20220205224724690](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205224724690.png)

---

- ### input 유형 - 일반

  - 일반적으로 입력을 받기 위하여 제공되면 타입별로 HTML 기본 검증 혹은 추가 속성을 활용할  수 있음
    - text : 일반 텍스트 입력
    - password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
    - email : 이메일 형식이 아닌 경우 form 제출 불가
    - number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
    - file : accept 속성을 활용하여 파일 타입 지정 가능

![image-20220205224912182](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205224912182.png)

---

- ### input 유형 - 항목 중 선택

  - 일반적으로 label을 사용하여 내용을 작성하여 항목 중 선택할 수 있는 input을 제공
  - 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 value를 지정해야 함
    - chechbox : 다중 선택
    - radio : 단일 선택

![image-20220205225045726](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205225045726.png)

---

- ### input 유형 - 기타

  - 다양한 종류의 input을 위한 picker를 제공
    - color : color picker
    - date : date picker
  - hidden input 을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
    - hidden : 사용자에게 보이지 않는 input

![image-20220205225245230](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205225245230.png)

---



## CSS(Cascading Style Sheets)

- 스타일을 지정하기 위한 언어

![image-20220205225420019](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220205225420019.png)



- ### 선택자(Selector) 유형

  - 기본 선택자
    - 전체 선택자, 요소 선택자
    - 클래스 선택자, 아이디 선택자, 속성 선택자
  - 결합자
    - 자손 결합자, 자식 결합자
    - 일반 형제 결합자, 인접 형제 결합자
  - 의사 클래스 / 요소
    - 링크, 동적 의사 클래스
    - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자



![image-20220212220153177](Web&CSS_사진모음/image-20220212220153177.png)





- ### CSS 선택자 정리

  - 요소 선택자
    - HTML 태그를 직접 선택
  - 클래스(class) 선택자
    - 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택
  - 아이디(id) 선택자
    - `#` 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
    - 일반적으로 하나의 문서에 1번만 사용. 여러 번 사용해도 동작하지만, 단일 id사용을 권장



- ### CSS 적용 우선순위

  - CSS 우선순위를 아래와 같이 그룹을 지어볼 수 있다.
    - 1. 중요도(Importance) - 사용시 주의 => `!important`
    - 2. 우선 순위(Specificity)
    - 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
    - 3. CSS 파일 로딩 순서



- ### CSS 상속

  - CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
    - 속성 중에는 상속이 되는 것과 되지 않는 것들이 있다.
  - 상속 되는 것
    - ex) Text 관련 요소(font, color, text-align) 등
  - 상속 되지 않는 것
    - ex) Box model 관련 요소(width, height, margin, padding)

![image-20220212221814595](Web&CSS_사진모음/image-20220212221814595.png)



## CSS 기본 스타일

- ### 크기 단위

  - px(픽셀)
    - 모니터 해상도의 한 화소인 '픽셀' 기준
    - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
  - %
    - 백분율 단위
    - 가변적인 레이아웃에서 자주 사용
  - em
    - (바로 위, 부모 요소에 대한) 상속의 영향을 받음
    - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
  - rem
    - (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
    - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
  - viewport
    - 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역 (디바이스 화면)
    - vw, vh, vmin, vmax



- ### 색상 단위

  - 색상 키워드
    - 대소문자를 구분하지 않음
    - red, blue, black 과 같은 특정 색을 직접 글자로 나타냄
  - RGB 색상
    - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
    - '#' + 16진수 표기법
    - rgb( ) 함수형 표기법
  - HSL 색상
    - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식
    - 색상, 채도, 명도



---



## Selectors 심화

### 결합자(Combinators)

- 자손 결합자
  - selectorA 하위의 모든 selectorB 요소
- 자식 결합자
  - selectorA 바로 아래의 selectorB 요소
- 일반 형제 결합자
  - selectorA의 형제 요소 중 뒤에 위치하는 selectorB 요소를 모두 선택
- 인접 형제 결합자
  - selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택



![image-20220212222707268](Web&CSS_사진모음/image-20220212222707268.png)



![image-20220212222723181](Web&CSS_사진모음/image-20220212222723181.png)



![image-20220212222733471](Web&CSS_사진모음/image-20220212222733471.png)



---



## CSS Box model

- ### 모든 요소는 <span style= "color: red">네모(박스모델</span>이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다. <span style = "color: red">(좌측 상단에 배치)</span>

![image-20220212222930650](Web&CSS_사진모음/image-20220212222930650.png)



- ##### 모든 HTML 요소는 box 형태도 되어 있음

- ##### 하나의 박스는 네 부분(영역)으로 이루어짐

  - content

  - ##### padding(상-우-하-좌)

  - border

  - ##### margin(상-우-하-좌)

![image-20220212223035357](Web&CSS_사진모음/image-20220212223035357.png)





![image-20220212223147736](Web&CSS_사진모음/image-20220212223147736.png)



---



## CSS 원칙 2

- 모든 요소는 네모(박스모델)이고, 좌측상단에 배치.

- ##### <span style = "color:red">display에 따라 크기와 배치가 달라진다.</span>



- #### 대표적으로 활용되는 display

  - display : block
    - 줄 바꿈이 일어나는 요소
    - 화면 크기 전체의 가로 폭을 차지한다.
    - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
    - ex)  div / ul, ol, li / p / hr / form 등

  

  - display : inline
    - 줄 바꿈이 일어나지 않는 행의 일부 요소
    - content 너비만큼 가로 폭을 차지한다.
    - width, height, margin-top, margin-bottom을 지정할 수 없다.
    - 상하 여백은 line-height로 지정한다.
    - ex)  span / a / img / input, label / b, em, i, strong 등

  

  - display : inline-block
    - block과 inline 레벨 요소의 특징을 모두 가짐
    - inline처럼 한 줄에 표시 가능하고, block처럼 width, height, margin 속성을 모두 지정할 수 있음

  

  - display : none
    - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
    - 이와 비슷한 visibility : hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.

![image-20220212224026034](Web&CSS_사진모음/image-20220212224026034.png)



---



## CSS Position

- static : 모든 태그의 기본 값(기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨
- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
  - relative
  - absolute
  - fixed



- relative : 상대 위치
  - 자기 자신의 static 위치를 기준으로 이동 (normal flow 유지)
  - 레이아웃에서 요소가 차지하는 공간을 static 일 때와 같음 (normal position 대비 offset)

- absolute : 절대 위치
  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
  - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동 (없는 경우 body)
- fixed : 고정 위치
  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
  - 부모 요소와 관계없이 viewport를 기준으로 이동
    - 스크롤 시에도 항상 같은 곳에 위치함(`sticky`도 있지만 조금 다름)



![image-20220212224616871](Web&CSS_사진모음/image-20220212224616871.png)



![image-20220212224631795](Web&CSS_사진모음/image-20220212224631795.png)



![image-20220212224639829](Web&CSS_사진모음/image-20220212224639829.png)



![image-20220212224651285](Web&CSS_사진모음/image-20220212224651285.png)



![image-20220212224742388](Web&CSS_사진모음/image-20220212224742388.png)



![image-20220212224754438](Web&CSS_사진모음/image-20220212224754438.png)



---



## 개발자 도구

- 주요 기능
  - Elements : DOM 탐색 및 CSS 확인 및 변경
    - Styles : 요소에 적용된 CSS 확인
    - Computed : 스타일이 계산된 최종 결과
    - Event Listeners : 해당 요소에 적용된 이벤트(JS)



![image-20220212224948207](Web&CSS_사진모음/image-20220212224948207.png)



![image-20220212224959861](Web&CSS_사진모음/image-20220212224959861.png)



![image-20220212225014216](Web&CSS_사진모음/image-20220212225014216.png)



![image-20220212225038302](Web&CSS_사진모음/image-20220212225038302.png)





## 추가 컨텐츠

- MDN web docs
  - [mozilla](https://developer.mozilla.org/ko/)

- 개발자 도구 활용법
  - [chrome developer](https://developer.chrome.com/docs/devtools/css/)

- Emmet
  - HTML & CSS를 작성할 때 보다 빠른 마크업을 위해서 사용되는 오픈소스
  - 단축키, 약어 등을 사용
  - 대부분의 텍스트 에디터에서 지원
  - [Emmet](https://emmet.io/)
  - [Emmet docs](https://docs.emmet.io/cheat-sheet/)



## 마무리

- 웹과 브라우저의 변화, 그리고 표준.
- HTML 기본 구조
  - 요소, 태그, DOM 트리
- HTML 다양한 태그들
  - 그룹, 텍스트 관련 요소
  - `<table>` `<form>` 등
- HTML은 보이는 것 이상의 의미를 가지기도 한다.
  - 메타태그, 시멘틱 태그 등을 통한 SEO
  - 웹 접근성



- CSS 기초 문법
- CSS 선택자 및 우선 순위
- CSS Box model
- CSS Display
- CSS Position



- HTML : 웹 페이지가 어떻게 구조화되어 있는지 알 수 있도록 하는 마크업 언어
- CSS : 사용자에게 문서(HTML)를 표시하는 방법을 지정하는 언어

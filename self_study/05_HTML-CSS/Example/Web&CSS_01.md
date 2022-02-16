### 1. HTML 정의

**문제 1) **아래의 보기 (1) ~ (4) 중에서, HTML의 본딧말을 고르시오. 

```
(1) Hyperlinks and Text Markup Language
(2) Home Tool Markup Language
(3) Hyper Text Markup Language
(4) Hyper Tool Markup Language
```



code

```
(3) Hyper Text Markup Language - 웹 페이지를 작성(구조화)하기 위한 언어이다.
```



---



### 2. HTML 개념

**문제 2) **각 문항을 읽고 맞으면 T, 틀리면 F를 작성 하시오.

```
1) 웹 표준을 만드는 곳은 Mozilla 재단이다.
2) 표(table) 을 만들 때에는 반드시 <th> 태그를 사용해야 한다.
3) 제목(Heading) 태그는 제목 이외에는 사용하지 않는 것이 좋다.
4) 리스트를 나열하기 위해서는 <ul> 태그만 사용 할 수 있다.
5) HTML의 태그는 반드시 별도의 닫는 태그가 필요하다. 
```



code

```
(1) F → 웹 표준을 만드는 곳은 `W3C`,`WHATWG`이다.
(2) F → 표(table)을 만들 때에는 <tr>으로 가로 줄을 구성하고 내부에는 <th> 혹은 <td>로 셀을 구성하지만 반드시 `th`를 사용해야할 필요는 없다.
(3) T → 시맨틱 태그들은 그 의미에 맞도록 사용하는 것이 권장된다.
(4) F → <ol></ol> : 순서가 있는 리스트 (ordered)
		<ul></ul> : 순서가 없는 리스트 (unordered)
(5) F → 여는 태그와 닫는 태그가 한 쌍인 태그와 별도의 닫는 태그가 필요하지 않은 태그가 존재한다.
	ex) <br>, <img>, <hr>, <input>
```



### 3. CSS 정의

**문제 3) **아래의 보기 (1) ~ (4) 중에서, CSS의 본딧말을 고르시오. 

```
(1) Creative Style Sheets
(2) Cascading Style Sheets
(3) Computer Style Sheets
(4) Colorful Style Sheets
```



code

```
(2) Cascading Style Sheets
```



### 4. CSS 개념

**문제 4) **각 문항을 읽고 맞으면 T, 틀리면 F를 작성 하시오.

```
1) HTML과 CSS는 각자 문법을 갖는 별개의 언어이다.
2) 웹 브라우저는 내장 기본 스타일이 있어 CSS가 없어도 작동한다.
3) 자식 요소 프로퍼티는 부모의 프로퍼티를 모두 상속 받는다.
4) 디바이스마다 화면의 크기가 다른 것을 고려하여 상대 단위인 %를 사용한다.
5) id 값은 유일해야 하므로 중복되어서는 안된다.
```



code

```
(1) T → HTML과 CSS는 같은 파일 안에 작성될 수는 있지만, 별개의 언어이다.
(2) T → 웹 브라우저 별로 내장 기본 스타일(user agent stylesheets)이 있다.
        그래서 Bootstrap 같은 CSS Framework는 모든 브라우저가 똑같은 출발선에서 CSS가 작성될 수             있도록 하는 reset.css 같은 초기화 css를 포함하고 있다.
(3) F → 모두 상속받지 않는다.
        대표적으로 width, height, background-color 와 같은 속성들은 상속되지 않는다.
(4) F → 디바이스에 따른 상대 단위는 `vw`, `vh` 를 사용한다.
  		백분율 값은 요소의 부모의 크기를 참조하므로 각각의 사용 용도가 다르다.
(5) T → id 값은 반드시 고유 값이어야 한다.
```



### 5. CSS 우선순위

**문제 5) **CSS는 우선 적용되는 순서가 존재 한다. 우선순위가 높은 순으로 나열 하시오.

```
요소 선택자,		Inline style,		소스 순서,
!important, 	id 선택자, 		class선택자
```



code

```
1. !important(속성값 뒤에 !important가 붙어있는 속성)
2. Inline style('html 파일에서 스타일 직접 지정'으로 적용되어 있는 속성)
3. id 선택자(선택자에 id가 쓰인 속성)
4. class 선택자(class, attribute, pseudo-class로 지정한 속성)
5. 요소 선택자(태그 이름으로 지정한 속성)
6. 소스 순서(부모 요소에 의해 상속된 속성)
```

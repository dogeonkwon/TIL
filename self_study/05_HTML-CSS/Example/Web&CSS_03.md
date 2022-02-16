### 1. Semantic Tag

**문제 1) **보기 중 콘텐츠의 의미를 명확히 하기 위해 HTML5에서 새롭게 추가된 시맨틱(semantic) 태그를 모두 고르시오.

```
div, header, h1, section, footer, a, form, span
```



code

```
대표적인 태그 목록
→ header : 문서 전체나 섹션의 헤더(머리말 부분)
→ section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
→ footer : 문서 전체나 섹션의 푸터(마지막 부분)
```



---



### 2.  input Tag

**문제 2) **아래 이미지와 같이 로그인 Form을 생성하는 HTML코드를 작성하시오. 단, USERNAME 글자를 클릭하면 아이디를 입력하는 input에, PWD 글자를 클릭하면 비밀번호를 입력하는 input에 focusing 되도록 하시오.



![image-20220204203928530](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220204203928530.png)



code

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <form action="">
    <div class="input-group">
      <label for="username">USERNAME : </label>
      <input type="text" name="username" placeholder="아이디를 입력 해 주세요." id="username" autofocus>
    </div>

    <form action=""></form>
      <div class="input-password">
        <label for="pwd">PWD : </label>
        <input type="password" name="pwd" value="111111111" id="pwd" autofocus>
        <button type="submit">제출</button>
      </div>
  </form>
</body>
</html>
```



---



### 3. 크기 단위

**문제 3) **크기 단위 em은 요소에 지정된 상속된 사이즈나 기본 사이즈에 대해 상대적인 사이즈를 설정한다. 즉, 상속의 영향으로 사이즈가 의도치 않게 변경될 수 있는데 이를 예방하기 위해 HTML 최상위 요소의 사이즈를 기준으로 삼는 크기 단위는 무엇인가?



code

```
rem : 최상위 요소인 html요소의 크기에 대해 영향을 받아 크기가 변함
```

- em : 부모 요소의 크기의 영향을 받아 크기가 변함
- rem : 최상위 요소인 html요소의 크기에 대해 영향을 받아 크기가 변함
- % : 부모 요소의 크기의 영향을 받아 크기가 변함



---



### 4. 선택자

**문제 4) **다음 예제를 통해 ‘자손 결합자’와 ‘자식 결합자’의 차이를 설명하시오.



![image-20220204204043661](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220204204043661.png)



code

```
자손 결합자 : div p → div 요소에 포함된 p 요소를 선택한다. (자손 관계)
자식 결합자 : div > p → div 요소의 직계 자식 요소인 p를 선택한다. (자식 관계)

자손은 해당 앞에 나온 태그에 포함 되어 있는 관계이며 자식은 앞에 나온 태그에 바로 인접한 관계를 뜻 한다.
```



### 1. Semantic Tag

**문제 1) **제시된 semantic.html과 semantic.css를 수정하여 다음 이미지와 같은 형태가 되도록 코드를 작성하시오.

![image-20220204230224897](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220204230224897.png)



code(html)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="semantic.css">
  <title>Layout Practice</title>
</head>
<body>
  <header class="header">
    <h1>header</h1>
  </header>
  <nav class="nav">
    <h2>nav</h2>
  </nav>
  <div class="clearfix">
    <section class="section">
      <h2>section</h2>
      <article class="article">
        <h3>article1</h3>
      </article>
      <article class="article">
        <h3>article2</h3>
      </article>
    </section>
    <aside class="aside">
      <h2>aside</h2>
    </aside>
  </div>  
  <footer class="footer">
    <h2>footer</h2>
  </footer>
</body>
</html>
```



code(css)

```css
/* 아래 코드는 수정하지 마세요. */
body {
  font-family: Arial;
  width: 800px;
}

section {
  float: left;
  margin-left: 4px;
}

aside { 
  float: right;
  margin-right: 4px;
}

.clearfix::after {
  content: "";
  display: block;
  clear: both;
}

/* 여기서부터 작성하세요. */
/* 모든 스타일 요소를 ***클래스***로 만들어 작성 후 사용합니다. */

/* 1. article 태그는 white로 나머지 시멘틱 태그는 lightgrey로 배경색을 바꿔주세요. */

.article {
  margin: 4px;
  text-indent: 3px;
  background-color: white;
  border-radius: 4px;
  border-width: 1px;
  border-style: solid;
  border-color: black;
}
.header, .nav, .footer {
  background-color: lightgrey;
  margin: 4px;
  padding: 4px;
  border-radius: 4px;
  border-width: 1px;
  border-style: solid;
  border-color: black;
}
.section {
  background-color: lightgrey;
  border-radius: 4px;
  border-width: 1px;
  border-style: solid;
  border-color: black;
  padding: 4px;
}
.aside {
  background-color: lightgrey;
  border-radius: 4px;
  border-width: 1px;
  border-style: solid;
  border-color: black;
  padding: 4px;
}
.footer {
  background-color: lightgrey;
  border-radius: 4px;
  border-width: 1px;
  border-style: solid;
  border-color: black;
}


/* 2. header, nav, footer 태그의 margin을 4px로 만들어주세요. */


/* 3. header, nav, footer 태그의 padding을 4px로 만들어주세요. */


/* 4. h1 태그를 수평 중앙 정렬 시켜주세요. */

.header {
  text-align: center;
  /* margin: auto;
  width: 30%; */
}


/* 5. section 태그는 width 490px height 300px, 
   aside 태그는 width 280px height 300px로 만들어주세요.*/

.section {
  width: 490px;
  height: 300px;
}
.aside {
  width: 280px;
  height: 300px;
}


/* 6. 모든 semantic 태그의 border 두께를 1px, 실선, 검은색으로 만들어주세요. */


/* 7. 모든 semantic 태그의 border 모서리 반경을 4px로 만들어주세요. */
```


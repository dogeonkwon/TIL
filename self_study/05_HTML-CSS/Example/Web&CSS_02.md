### 1. img tag

**문제 1) **아래 그림과 같은 폴더 구조가 있다. resume.html에서 코드를 작성 중일 때, image 폴더 안의 my_photo.png를 보여주는 ![img]() tag를 작성하시오. 단, 이미지가 제대로 출력되지 않을 때는 ssafy 문자열이 출력 되도록 작성하시오.



![image-20220204234050146](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220204234050146.png)



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
  
  <img src="c:\Users\Windows 10\Desktop\TIL\ssafy\image" alt="ssafy">

</body>
</html>
```



---



### 2. 파일 경로

**문제 2) **경로를 __(a)__로 작성 할 시, github에 업로드 하거나 전체 폴더의 위치가 변경 되었을 때 이미지를 불러 올 수 없게 된다. 이를 해결 하려면 이미지 경로를 __(b)__ 로 바꾸어 작성하면 된다. __(a)__와 __(b)__에 들어갈 말과 __(b)__ 로 변경한 코드를 작성하시오. 



```html
(a) - 절대경로
(b) - 상대경로

<img src="../ssafy/image" alt="ssafy">
```



### 3. Hyper Link

**문제 3) **출력된 my_photo.png 이미지를 클릭하면 ssafy.com으로 이동하도록 하시오.



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
  
  <a href="ssafy.com">
      <img src="c:\Users\Windows 10\Desktop\TIL\ssafy\image" alt="ssafy">
  </a>
  	

</body>
</html>
```



### 4. 선택자

**문제 4 - 1) ** 아래의 코드를 작성하고 결과를 확인 하시오.

```html
  <div id = "ssafy">
    <h2>어떻게 선택 될까?</h2>
    <p>첫번째 단락</p>
    <p>두번째 단락</p>
    <p>세번째 단락</p>
    <p>네번째 단락</p>
  </div>
```

```css
#ssafy > p:nth-child(2) {
  color: red;
}

=> 두번째 단락글자 빨간색으로 바뀜
```



**문제 4 - 2) **nth-child를 nth-of-type으로 변경하고 결과를 확인 하시오.

```css
#ssafy > p:nth-of-type(2) {
  color: blue;
}

=> 첫번째 단락글자 파란색으로 바뀜
```



**문제 4 - 3) **작성한 코드를 참고하여 nth-child()와 nth-of-type()의 차이점을 작성하시오

```
nth-child(n)
  - 부모의 n번째 자식을 찾고 해당 element 선택
  - 다른 element 모두 자식으로 선택하여 자식들 중, `n`번째를 찾는다.
  - 부모의 n번째 자식이 해당 element가 아니면 선택되지 않는다.

nth-of-type(n)
  - 부모의 n번째에 해당하는 element 선택
  - 다른 element들이 있어도 모두 자식으로 선택되지 않고 해당 element 만 선택되어 n번째를 찾는다.
```


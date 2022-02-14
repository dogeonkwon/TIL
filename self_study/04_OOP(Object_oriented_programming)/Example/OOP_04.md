### 1. 도형 만들기

**문제 ) ** 아래의 명세를 읽고 Python 클래스를 활용하여 점(Point)과 사각형(Rectangle)을 표현하시오.



Point 클래스에 대한 명세는 다음과 같다

![image-20220127174722712](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220127174722712.png)



![image-20220127174738460](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220127174738460.png)



![image-20220127174751792](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220127174751792.png)



code

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
class Rectangle(Point):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    def get_area(self):
        return abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y)

    def get_perimeter(self):
        return 2 * (abs(self.p1.x - self.p2.x) + abs(self.p1.y - self.p2.y))

    def is_square(self):
        return abs(self.p1.x - self.p2.x) == abs(self.p1.y - self.p2.y)


p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p1 = Point(3, 7)
p2 = Point(6, 4)
r1 = Rectangle(p1, p2)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())
```






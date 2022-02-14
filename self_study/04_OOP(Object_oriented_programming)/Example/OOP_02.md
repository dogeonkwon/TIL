##### Faker는 개발시 활용할 수 있는 가상의 데이터를 생성해주는 파이썬 패키지이다. 워크샵에 등장하는 코드는 모두 Github(https://github.com/joke2k/faker) 문서의 예제이다. 지금까지 배운 파이썬 개념을 활용하여 해석 하시오.



### 1. pip

**문제 1) ** 아래 명령어는 (1) 무엇을 위한 명령인지 (2) 실행은 어디에서 해야하는지 작성 하시오.

```python
$ pip install faker
```



code

```python
(1) faker 라는 패키지를 설치한다.

(2) 터미널(TERMINAL)
```



---



### 2. Basic Usages(https://github.com/joke2k/faker#basic-usage)

**문제 2) ** Faker는 다양한 메서드를 통해 임의의 결과값을 반환해준다. 임의의 영문 이름을 반환하는 아래 코드에서 라인별 의미를 주석을 참고하여 작성하시오.

```python
from faker import Faker  # 1 _______을 하기 위한 코드이다.
fake = Faker()			  # 2 Faker는 _____, fake는 ______이다.
fake.name()				  # 3 name()은 fake의 _____이다.
```



code

```python
1. # faker라는 모듈안에 있는 Faker이라는 클래스를 사용하기 위해 만든 코드이다.

2. # Faker()는 Class, fake는 instence이다.

3. # neme()은 fake의 메서드이다.
```



---



'김연아'는 실제로 존재하죠? 네, 여러분이 생각하시는 그 김연아 맞아요. ㅎㅎ '김동성'도 실제로 존재하죠? 두 사람 다 실제로 존재하는 사람입니다.

두 사람의 공통점은 무엇일까요? 여러 가지를 들 수 있겠지만 둘 다 '스케이터'라는 공통점을 갖고 있지요.

'스케이터'라는 단 하나의 사람이나 물건이 실제로 존재할까요? 그렇지는 않습니다. 하지만 우리는 '스케이트 타는 사람'을 '스케이터'라고 말합니다. 이런 것을 일컫는 말이 클래스(class)입니다. 우리 말로 옮기기는 쉽지 않지만 '부류'라는 의미로 생각하시면 좋을 것 같아요.

다른 예를 들어볼까요?

'사과'는 클래스이구요, '내가 엊저녁에 먹은 사과 다섯 개 중에 두 번째 것'이라고 콕 찍어서 말해주면 실체(instance)로 봐줄만합니다.

'좋은 집'은 실체일까요? 어느 한 집만을 콕 찍어서 '좋은 집'이라고 하기는 힘들 것 같군요. 그럼 '우리 집'은 실체일까요? 그건 실체라고 해도 될 것 같네요. 단, 집을 여러 채 가진 사람이 '우리 집'이라고 말할 때는 정확히 어느 집을 가리키는 것인지 알 수 없겠죠. 프로그램 작성을 위해 클래스를 설계하다보면 이런 애매한 문제를 만날 때도 있지요.

이제 파이썬으로 부류와 실체를 표현해보도록 하겠습니다.

```python
>>> class Singer:                      # 가수를 정의하겠느니라…
...     def sing(self):                # 노래하기 메서드
...            return "Lalala~"
...    
>>> taeji = Singer()                   # 태지를 만들어랏!
>>> taeji.sing()                       # 노래 한 곡 부탁해요~
'Lalala~'
```

클래스를 만들 때는 위와 같이 `class 클래스이름:` 형식으로 시작해서 그 다음부터 그 클래스의 성질이나 행동을 정의해주면 됩니다. 둘째 줄에는 함수가 정의되어 있죠? 이와 같이 클래스 내부에 정의된 함수를 메서드(method)라고 부릅니다.

여기서 sing 메서드는 Singer라는 클래스가 하는 행동을 정의하고 있죠. Singer 클래스를 만든 다음에는 taeji라는 객체를 만들었습니다. `인스턴스명 = 클래스()`와 같이 만들면 되죠.

그 다음엔 그렇게 만들어진 taeji에게 노래를 시켜봤습니다. Singer 클래스에 sing 메서드를 정의해줬기 때문에 Singer 클래스에 속한 taeji 객체도 sing 메서드를 사용할 수 있지요. 다시 말해서 가수는 노래할 수 있으니까 태지라는 가수도 역시 노래를 할 수 있는 것입니다. 이와 같이 어떤 객체의 메서드를 사용할 때는 `객체.메서드` 형식으로 해주시면 됩니다.

이번엔 같은 방법으로 리키 마틴 객체를 만들어서 노래를 청해보세요.



---



### 3. Localization(https://github.com/joke2k/faker#localization)

**문제 3) **아래의 코드를 실행 하였을 때, 변수 a와 b에 담긴 list의 요소가 같은지 혹은 다른지 여부를 판단하고 그 이유를 작성하시오.

1. 인자 없이 호출 시에는 영문이 기본 설정이다. (en_US)

```python
fake = Faker()
fake.name()
# => 'Shelly Wilcox' (랜덤이므로 결과 값이 다를 수 있음)
```

2. Locale 정보를 포함하여 호출 시에는 해당 언어 설정을 따른다.

```python
fake_ko = Faker('ko_KR')
fake_ko.name()
# => '박진우' (랜덤이므로 결과 값이 다를 수 있음)
```

직접 해당하는 기능을 구현한다고 하였을 때, 빈칸 (a), (b), (c)에 들어갈 코드로 적절한 것을 작성하시오. (힌트: 생성자 메서드와 함수의 개념)

```python
class Faker():
    
    def __(a)__((b), (c)):
        pass
```



code

```python
(a) : init
(b) : self
(c) : Locale
```



### 4. Seeding the Generator(https://github.com/joke2k/faker#seeding-the-generator)

컴퓨터 프로그래밍에서 임의의 값을 반환하는 경우(난수 생성 등) 시드라는 개념이 있다. 시드를 설정하게 되면 동일한 순서로 난수를 발생시킬 수 있어 일반적으로 디버깅을 위하여 활용 된다.

```python
import random

random.random()	# => 임의의 수
random.random()	# => 임의의 수

random.seed(7777)
print(random.random())

random.seed(7777)
print(random.random())
```



아래의 코드를 실행 했을 때, #1과 #2에서 출력되는 결과를 각각 작성하고, seed()는 어떤 종류의 메서드인지 작성하시오.

```python
fake = Faker('ko_KR')
Faker.seed(4321)

print(fake.name())		# 1. 이도윤 

fake2 = Faker('ko_KR')
print(fake2.name())		# 2. 이지후, 이지후, 이지후
```

- seed()는 Class 메서드이다.



### 4. Seeding the Generator

아래의 코드를 실행 했을 때, #1과 #2에서 출력되는 결과를 각각 작성하고, seed_instance()는 어떤 종류의 메서드인지 작성하시오.

```python
fake = Faker('ko_KR')
fake.seed_instance(4321)

print(fake.name())		# 1. 이도윤

fake2 = Faker('ko_KR')
print(fake2.name())		# 2. 이지훈, 전상훈, 이영호
```

- seed_instance()는 Instance 메서드이다.



seed()와 seed_instance()는 각각 어떠한 용도로 쓰일 수 있는지 작성하시오.

- seed()는 class에 적용되어 class전체에 난수를 발생시키고, seed_instance()는 instance에 적용되어 instance에 난수를 발생시킨다.


# 1. 배열

- ### 알고리즘

- ### 배열

- ### 버블 정렬(Bubble Sort)

- ### 카운팅 정렬(Counting Sort)

- ### 완전검색

- ### 그리디(Greedy Algorithm)



----



- ### 알고리즘

  - 컴퓨터 분야에서 알고리즘을 표현하는 방법은 크게 두 가지
    - 의사코드(슈도코드, Pseudocode)와 순서도



![image-20220209083558322](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209083558322.png)

- #### 무엇이 좋은 알고리즘인가?

  - 정확성 : 얼마나 정확하게 동작하는가
  - 작업량 : 얼마나 적은 연산으로 원하는 결과를 얻어내는가
  - 메모리 사용량 : 얼마나 적은 메모리를 사용하는가
  - 단순성 : 얼마나 단순한가
  -  최적성 : 더 이상 개선할 여지없이 최적화되었는가



- ##### 알고리즘의 작업량을 표현할 때 **시간복잡도**로 표현한다.



- #### 시간 복잡도 = 빅-오(O) 표기법

  - 시간 복잡도 함수 중에서 가장 큰 영향력을 주는 n에 대한 항만을 표시
  - 계수는 생략하여 표시



![image-20220209083913377](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209083913377.png)



![image-20220209084146514](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209084146514.png)



---



- ### 배열

- 1차원 배열의 선언

  - 별도의 선언 방법이 없으면 변수에 처음 값을 할당할 때 생성
  - 이름 : 프로그램에서 사용할 배열의 이름



![image-20220209084309264](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209084309264.png)



- ##### 배열 활용 예제 : Gravity

  - 상자들이 쌓여있는 방이 있다. 방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때, 낙차가 가장 큰 상자를 구하여 그 낙차를 리턴 하는 프로그램을 작성하시오.
  - 중력은 회전이 완료된 후 적용된다.
  - 상자들은 모두 한쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며 벽에서 떨어져서 쌓인 상자는 없다.
  - 방의 가로길이는 항상 100이며, 세로 길이도 항상 100이다.
  - 즉, 상자는 최소 0, 최대 100 높이로 쌓을 수 있다.
  - **그림 설명**



![image-20220209084642800](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209084642800.png)



```python
# 낙차가 가장 큰 상자를 구해야 하며 벽의 최대 높이가 100이므로 100을 설정한다
N = 100

# 상자가 쌓여진 정도를 입력 받는다.(예제는 7 4 2 0 0 6 0 7 0)
box_count = list(map(int, input().split()))

# 상자가 쌓인 방의 가로 길이를 구한다.
cnt = 0
for n in box_count:
    cnt += 1

# 방안에서 상자가 얼마나 떨어졌는지를 알아보기 위하여 그 길이만큼의 빈 리스트를 만든다.
count_right = [0] * cnt
count_left = [0] * cnt

# 오른쪽으로 떨어질 때! 첫 번째 값이 오른쪽 값보다 클 때마다 한 칸씩 떨어질 수 있다는 의미이므로 count_right[i]에 1씩을 더해준다.
for i in range(cnt):
    for j in range(i+1, cnt):
        if box_count[i] > box_count[j]:
            count_right[i] += 1

# 오른쪽으로 떨어질 때! 마지막 값이 가장 큰 값이 될 수 있도록 만들어준다.
for l in range(cnt-1):
    if count_right[l] > count_right[l+1]:
        count_right[l+1] = count_right[l]



# 왼쪽으로 떨어질 때! 마지막 값이 왼쪽 값보다 클 때마다 한 칸씩 떨어질 수 있다는 의미이므로 count_left[i-1]에 1씩을 더해준다.
for i in range(cnt, 0, -1):
    for j in range(i, 0, -1):
        if box_count[i-1] > box_count[j-1]:
            count_left[i-1] += 1


# 왼쪽으로 떨어질 때! 마지막 값이 가장 큰 값이 될 수 있도록 만들어준다.
for l in range(cnt-1, 0 , -1):
    if count_right[l] > count_right[l-1]:
        count_right[l-1] = count_right[l]

# 오른쪽으로 떨어질 때와 왼쪽으로 떨어질 때 중 어느 값이 더 큰지를 비교하기 위해 count_right[-1]과 count_left[-1]을 비교하여 출력한다.
# 그리고 방의 가로길이를 뺀 나머지 높이를 더해줄 수 있도록 (N - cnt)를 더해준다.
if count_right[-1] > count_left[-1]:
    print(count_right[-1] + (N - cnt))
else:
    print(count_left[-1] + (N - cnt))
```





- ##### 2개 이상의 자료를 특정 기준에 의해 작은 값부터 큰 값(<span style= 'color: red'>오름차순</span>), 혹은 그 반대의 순서대로(<span style = 'color : red'>내림차순</span>) 재배열 하는 것 



- #### 대표적인 정렬 방식의 종류

  - 버블 정렬 (Bubble Sort)
  - 카운팅 정렬 (Counting Sort)
  - 선택 정렬 (Seletion Sort)
  - 퀵 정렬 (Quick Sort)
  - 삽입 정렬 (Insertion Sort)
  - 병합 정렬 (Merge Sort)



---



- ### 버블 정렬

- ##### 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

- ##### 정렬 과정

  - 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막자리까지 이동한다.
  - 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
  - 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같다고 하여 버블정렬이라 한다.

- ##### 시간 복잡도 : O(n**2)



```python
def bubble_sort(a, N):      # 오름차순
    for i in range(N-1, 0, -1):      # 정렬 구간의 끝
        for j in range(i):          #비교할 왼쪽원소
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return

#--------------------------------------------------------------------

# 버블정렬 사용

T = int(input())        # TC 개수
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    bubble_sort(arr, N)
    print(f'#{tc}', end=' ')
    # for x in arr:
    #     print(x, end =' ')			# 밑의 *처럼 사용안하면 주석처럼 사용해야 한다.
    # print()
    print(*arr)
```





- ##### [55, 7, 78, 12, 42]를 버블 정렬하는 과정 (오름차순)

![image-20220209085432287](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209085432287.png)



![image-20220209085451167](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209085451167.png)



![image-20220209085504693](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209085504693.png)



![image-20220209085516444](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209085516444.png)



- #### 배열을 활용한 버블 정렬

  - 앞서 살펴 본 정렬 과정을 코드로 구현하면 아래와 같다. (오름차순)

![image-20220209085556992](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209085556992.png)



---



- ### 카운팅 정렬

- ##### 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘

- ##### 제한 사항

  - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능 : 각 항목의 발생 회수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문이다.
  - 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다.

- ##### 시간 복잡도 : O(n + k) - n은 리스트 길이, k는 정수의 최대값



- ##### [0, 4, 1, 3, 1, 2, 4, 1] 을 카운팅 정렬하는 과정



![image-20220209085949876](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209085949876.png)



![image-20220209090008066](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209090008066.png)



![image-20220209090017877](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209090017877.png)



![image-20220209090027721](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209090027721.png)



![image-20220209090155883](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209090155883.png)



![image-20220209090208711](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209090208711.png)



![image-20220209090221962](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209090221962.png)



![image-20220209090234368](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209090234368.png)



![image-20220209090246437](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209090246437.png)



![image-20220209090304788](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209090304788.png)



![image-20220209090333638](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209090333638.png)



---



|  알고리즘   | 평균 수행시간 | 최악 수행시간 | 알고리즘 기법 | 비고                                                      |
| :---------: | :-----------: | :-----------: | :-----------: | :-------------------------------------------------------- |
|  버블 정렬  |    O(n**2)    |    O(n**2)    |  비교와 교환  | 코딩이 가장 손쉽다.                                       |
| 카운팅 정렬 |   O(n + k)    |   O(n + k)    |  비교환 방식  | n이 비교적 작을 때만 가능하다.                            |
|  선택 정렬  |    O(n**2)    |    O(n**2)    |  비교와 교환  | 교환의 회수가 버블,<br />삽입정렬보다 작다.               |
|   퀵 정렬   |  O(n log n)   |    O(n**2)    |   분할 정복   | 최악의 경우 O(n**2) 이지만,<br />평균적으로는 가장 빠르다 |
|  삽입 정렬  |    O(n**2)    |    O(n**2)    |  비교와 교환  | n의 개수가 작을 때 효과적이다.                            |
|  병합 정렬  |  O(n log n)   |  O(n log n)   |   분할 정복   | 연결리스트의 경우 가장 효율적인 방식                      |



---



- ##### 예제) Baby-gin Game

  - 0 ~ 9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를  갖는 경우를 run이라 하고, 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.
  - 그리고, 6장의 카드가 run과 triplet로만 구성된 경우를 bab-gin이라 부른다.
  - 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성하라.



```python
# 숫자를 연속해서 입력한다는 가정(6개 자리)
num = list(map(int, input()))

# run에서 연속된 세 자리를 구하는데 9번째 자리에서 index error가 나지 않게 하기 위해 12개의 리스트 자리를 만들어 준다.
counts = [0] * 12

# 6개 자리의 숫자를 따로 구분해서 개수가 얼만큼 있는지 확인하는 방법
for i in range(6):
    counts[num[i]] += 1     # 1번째 방법

    # c[num % 10] += 1
    # num //= 10        # 2가지 방법이 있다.(일반적으로 많이 사용하는 코드, while문을 사용해야 함)


# 별개의 검사를 하기 위해 if문을 2개 사용한다. 하나는 triplet(3장의 카드가 동일한 번호를 갖는 경우), 하나는 run(3장의 카드가 연속적인 번호를 갖는 경우)을 검사한다.
i = 0
tri = run = 0
while i < 10:
    if counts[i] >= 3:
        counts[i] -= 3
        tri += 1
        continue

    # run 조사 후 데이터 삭제
    if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
        counts[i] -= 1
        counts[i+1] -= 1
        counts[i+2] -= 1
        run += 1
        continue
    i += 1

# run과 tri의 합이 2가 되면 'Baby Gin' 이고 아니라면 'Lose'를 출력하게 한다.
if run + tri == 2:
    print('Baby Gin')
else:
    print('Lose')
```



---



- #### 순열

- 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것 (Factorial)



![image-20220209120907393](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220209120907393.png)



---



- ### 탐욕(Greedy) 알고리즘

- 최적해를 구하는 데 사용되는 근시안적인 방법
- 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달한다.
- 각 선택의 시점에서 이루어지는 결정은 지역적으로는 최적이지만, 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 하여, 그것이 최적이라는 보장은 없다



- 탐욕 알고리즘 동작 과정
  - 1) 해 선택 : 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해 집합(Solution Set)에 추가한다.
    2) 실행 가능성 검사 : 새로운 부분해 집합이 실행 가능한지를 확인한다.
    3) 해 검사 : 새로운 부분해 집합이 문제의 해가 되는지를 확인한다. 아직 전체 문제의 해가 완성되지 않았다면 (1)의 해 선택부터 다시 시작한다.



- ##### 예제) 거스름돈 줄이기 

  - "어떻게 하면 손님에게 거스름돈으로 주는 지폐와 동전의 개수를 최소한으로 줄일 수 있을까?"
  - 1. 해 선택 : 단위가 큰 동전으로만 거스름돈을 만들면 동전의 개수가 줄어듬으로 현재 고를 수 있는 가장 단위가 큰 동전을 골라 거스름돈에 추가한다.
    2. 실행 가능성 검사 : 거스름돈이 손님에게 내드려야 할 액수를 초과하는지 확인한다. 초과한다면 마지막에 추가한 동전을 거스름돈에서 빼고, (1)로 돌아가서 현재보다 한 단계 작은 단위의 동전을 추가한다.
    3. 해 검사 : 더 드려도, 덜 드려도 안되기 때문에 거스름돈을 확인해서 액수가 모자라면 다시 (1)로 돌아가서 거스름돈에 추가할 동전을 고른다.



---



### 알고리즘 기본기

- ##### 최대값을 구하는 방법

```python
# 최대값을 구하는 방법

arr = [2, 7, 3, 5, 4, 7]

maxv = arr[0]
for i in range(1, len(arr)):
    if maxv < arr[i]:
        maxv = arr[i]
print(arr[-1])
```



- ##### 최대값의 위치를 구하는 방법(첫 번째 수)

```python
# 최대값의 위치를 구하는 방법(첫 번째 수)

arr = [2, 7, 3, 5, 4, 7]

max_idx = 0
for i in range(1, len(arr)):
    if arr[max_idx] < arr[i]:
        max_idx = i
print(max_idx)
```



- ##### 최대값의 위치를 구하는 방법(마지막 번째 수)

```python
# 최대값의 위치를 구하는 방법(마지막 번째 수)

arr = [2, 7, 3, 5, 4, 7]

max_idx = 0
for i in range(1, len(arr)):
    if arr[max_idx] <= arr[i]:
        max_idx = i
print(max_idx)
```


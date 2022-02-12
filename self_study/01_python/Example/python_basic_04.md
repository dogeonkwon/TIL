1. 간단한 N의 약수 (SWEA #1933)

   

   ```python
   # range함수를 사용했을 때
   
   N = int(input()) # input받는 값
   
   # a를 b로 나눴을 때 나머지가 0 -> b는 a의 약수
   for n in range(1, N+1):
       if N % n == 0:
           print(n, end = '')
           
           
           
   # range함수를 사용하지 않고 풀어보았다.
   n = int(input())
   
   i = 1
   
   while i <= n:
       if n % i:		# n을 i로 나누었을 때 나머지가 있다면 n의 약수가 아니다.
           i += 1
       else:			# 나머지가 없다면 n의 약수이다.
           print(i, end = ' ')
           i += 1
   ```

   

2. 중간값 찾기 (SWEA #2063 변형)

   numbers = [ 85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24 ]
   
   ```python
   # 동기들이 푼 풀이를 그대로 가져왔다.
   
   numbers = [ 85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24 ]
   
   cnt = 0
   for i in numbers:
       cnt += 1
       
   for i in range(cnt): 
   	for j in range(cnt): 
        	if numbers[i]<=numbers[j]:
           	numbers[i], numbers[j] = numbers[j], numbers[i]
   
   if cnt % 2:
       print(numbers[cnt//2])
   else:
       print(numbers[cnt//2-1])
       
       
   # 내가 풀어보았다.
   
   numbers = [ 85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24 ]
   
   
   cnt = 0
   for i in numbers:		# range를 사용하기 위해 cnt를 구해준다.
       cnt += 1
   
   for i in range(cnt):		# range의 숫자대로 정렬한다.
       for j in range(cnt):		
           if numbers[i] >= numbers[j]:	# 앞의 숫자와 비교해서 앞의 수가 더 크면 뒤로 이동
               numbers[i], numbers[j] = numbers[j], numbers[i]
   
   if cnt % 2:
       result = numbers[cnt // 2]		# 리스트는 0부터 시작하기 때문에 // 2 만 해줘도 된다.
       print(result)
   else:
       result = numbers[cnt // 2 - 1]  # 짝수일 경우 // 2 를 해주고 - 1을 해준다.
       result2 = numbers[cnt // 2]		# 두 개 출력
       print(result, result2)
   ```
   
   
   
3. 계단 만들기

   

   ```python
   # 동기들이 푼 풀이
   
   n = int(input())
   i = 1
   
   while i < n + 1:
       j = 1
       while j < i + 1:
           print(j, end = ' ')
           j += 1
       print()
       i += 1
   
       
   # 내가 푼 풀이    
       
   number = int(input())
   
   i = 1
   while i <= number:			# 세로 줄을 만들어 준다.
       j = 1					# j가 계속 1로 시작할 수 있도록 해준다.
       while j <= i:			# i만큼만 커지도록 제한한다.
           print(j, end=' ')
           j += 1
       print('')				# 줄 간격을 띄우기 위해 넣었다.
       i += 1
   ```
import sys

n = int(sys.stdin.readline())
sequence = list()   # 처음 입력받은 수열
temp = list()       # 그 수열을 내림차순 시켜 작은 값부터 pop하기 위한 리스트
ans = list()        # +, - 를 기록해줄 리스트

for _ in range(n):         # 기준 수열과 정렬하여 pop하기 위한 리스트를 입력 받음
    k = int(sys.stdin.readline())
    sequence.append(k)
    temp.append(k)

temp.sort(reverse=True)     # temp 내림차순 정렬(뒤에서 부터 빼기 위해)
m = 0           # 기존 수열의 값의 인덱스를 찾아서 비교하기 위한 임의의 수

sub = list()        # 임시 리스트(완성되면 기존 수열과 비교)
sub2 = list()       # sub에 가기 전 잠시 머물 리스트
while temp:
    if sub2 and sequence[m] == sub2[-1]:    # sub2에 값이 있고 기존 수열과 그 마지막 값이 같다면 조건문 실행
        ans.append('-')
        sub.append(sub2.pop())
        m += 1
    else:           # temp에 값이 남아 있다면
        sub2.append(temp.pop())
        ans.append('+')

while sub2:         # 아직 sub2에 값이 남아 있다면 sub로 하나씩 옮겨준다.
    sub.append(sub2.pop())
    ans.append('-')

if sub == sequence: # sub와 sequence가 같다면 ans 하나씩 출력
    for j in ans:
        print(j)
else:               # 아니라면 'NO'를 출력
    print('NO')
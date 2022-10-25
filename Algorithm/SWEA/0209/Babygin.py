# Baby-gin 풀이
# 2022-02-09

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
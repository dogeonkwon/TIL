# 부분집합 풀이
# 2022-02-14

# 길이를 구하기 위한 lst_len 함수를 설정!
def lst_len(arr):

    cnt = 0
    for _ in arr:
        cnt += 1
    return cnt



N = list(map(int, input().split()))


# 비트 연산자를 이용하여 모든 조합을 구해보도록 하자!
for i in range(1<<lst_len(N)):

    # 큰 for문이 한 번 돌때마다 빈 리스트를 만들어 주도록 하자!
    lst = []

    for j in range(lst_len(N)):

        # 만약 i의 이진수가 (1<<j)의 이진수와 같다면 빈 리스트인 lst에 [N[j]](이렇게 해야 리스트 형태로 모여서 담김, append 함수를 쓰지 않기 위해)을 넣어줘라!
        if i & (1<<j):
            lst += [N[j]]

    # 그리고 for문과 if문을 이용하여 lst의 값 하나씩을 더해보고 0이 된다면 출력!
    total = 0
    for k in lst:
        total += k
    if total == 0:
        print(lst)

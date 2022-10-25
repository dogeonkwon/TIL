# 1206_View 풀이
# 2022-02-09
# s1

# 테스트 케이스를 얼만큼 받을지 입력한다.
T = 10


# 주어진 테스트 케이스만큼 출력하기 위한 for문을 만들어 준다.
for tc in range(1, T+1):

    # 입력하고 싶은 빌딩 숫자를 입력한다.
    K = int(input())

    # 빌딩의 숫자를 리스트 형식으로 입력한다.
    building_count = list(map(int, input().split()))

    # building_count의 길이를 구한다.
    cnt = 0
    for _ in building_count:
        cnt += 1

    # 조망이 확보된 세대 수를 세기 위하여 view_count 변수를 0으로 만들어 준다.
    view_count = 0

    # 앞의 두 자리와 끝의 두 자리는 0의 값을 가지므로 제외 시키고 for문을 구현한다.
    for i in range(2, cnt-2):
         # 조망이 확보된 세대수를 확인하기 위해서는 좌, 우로 2칸씩의 여유가 있어야한다.
         # 따라서 기준 빌딩에서 왼쪽 첫 번째와 두 번째 값을 빼고
         # 기준 빌딩에서 오른쪽 첫 번째와 두 번째 값을 뺀다.
        left_comparison = (building_count[i] - building_count[i-1])
        left_comparison_2 = (building_count[i] - building_count[i-2])

        right_comparison = (building_count[i] - building_count[i+1])
        right_comparison_2 = (building_count[i] - building_count[i+2])

        # 이러한 값들을 리스트 형식으로 모아준다.
        building_lst = [left_comparison, left_comparison_2, right_comparison, right_comparison_2]

        # 하나라도 음수가 나온다면 조망이 확보되지 않은 것이므로 모든 양수인지 체크해준다.
        if building_lst[0] > 0 and building_lst[1] > 0 and building_lst[2] > 0 and building_lst[3] > 0:

            # 그리고 모두 양수인 리스트가 들어왔다면 오름차순 정렬을 할 수 있도록 한다. 또한 무조건 길이는 4이므로 range(3)을 입력한다.
            # 정렬된 리스트의 첫 번째 값을 조망이 확보된 세대 수를 구하기 위해 view_count에 building_lst[0]을 누적시켜준다.
            for j in range(3):
                if building_lst[j] > building_lst[j + 1]:
                    building_lst[j + 1], building_lst[j] = building_lst[j], building_lst[j + 1]
            view_count += building_lst[0]
            print(view_count)

    # 정해진 양식에 맞게 출력한다.
    print('#{} {}'.format(tc, view_count))
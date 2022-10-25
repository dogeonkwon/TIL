# # Gravity 풀이
# # 2022-02-09

# # 낙차가 가장 큰 상자를 구해야 하며 벽의 최대 높이가 100이므로 100을 설정한다
# N = 100
#
# # 상자가 쌓여진 정도를 입력 받는다.(예제는 7 4 2 0 0 6 0 7 0)
# box_count = list(map(int, input().split()))
#
# # 상자가 쌓인 방의 가로 길이를 구한다.
# cnt = 0
# for n in box_count:
#     cnt += 1
#
# # 방안에서 상자가 얼마나 떨어졌는지를 알아보기 위하여 그 길이만큼의 빈 리스트를 만든다.
# count_right = [0] * cnt
# count_left = [0] * cnt
#
# # 오른쪽으로 떨어질 때! 첫 번째 값이 오른쪽 값보다 클 때마다 한 칸씩 떨어질 수 있다는 의미이므로 count_right[i]에 1씩을 더해준다.
# for i in range(cnt):
#     for j in range(i+1, cnt):
#         if box_count[i] > box_count[j]:
#             count_right[i] += 1
#
# # 오른쪽으로 떨어질 때! 마지막 값이 가장 큰 값이 될 수 있도록 만들어준다.
# for l in range(cnt-1):
#     if count_right[l] > count_right[l+1]:
#         count_right[l+1] = count_right[l]
#
#
#
# # 왼쪽으로 떨어질 때! 마지막 값이 왼쪽 값보다 클 때마다 한 칸씩 떨어질 수 있다는 의미이므로 count_left[i-1]에 1씩을 더해준다.
# for i in range(cnt, 0, -1):
#     for j in range(i, 0, -1):
#         if box_count[i-1] > box_count[j-1]:
#             count_left[i-1] += 1
#
#
# # 왼쪽으로 떨어질 때! 마지막 값이 가장 큰 값이 될 수 있도록 만들어준다.
# for l in range(cnt-1, 0 , -1):
#     if count_right[l] > count_right[l-1]:
#         count_right[l-1] = count_right[l]
#
# # 오른쪽으로 떨어질 때와 왼쪽으로 떨어질 때 중 어느 값이 더 큰지를 비교하기 위해 count_right[-1]과 count_left[-1]을 비교하여 출력한다.
# # 그리고 방의 가로길이를 뺀 나머지 높이를 더해줄 수 있도록 (N - cnt)를 더해준다.
# if count_right[-1] > count_left[-1]:
#     print(count_right[-1] + (N - cnt))
# else:
#     print(count_left[-1] + (N - cnt))


# # Gravity 풀이
# # 2022-02-09
# # 오른쪽으로 돌렸을 때 남은 공간의 길이 구하기
#
# N = 9
#
# # 박스 갯수를 담을 list
# box = list(map(int, input()))  # 8보다 작은 수를 입력해야 함, [7,4,2,0,0,6,0,7,0]
#
# # 낙차를 계산할 list
# Falling = [0] * 9
#
# # 0번 항목을 계산한다고 하면, box[1~7] 에서 box[0] 숫자와 크거나 같은 값이 없다면 낙차값 1을 더한다.
# for i in range(0, N):  # i = 0~7
#     cnt = 0
#     for j in range(1 + i, N):  # j = 1~8 , i가 7되면 (8,8)이 되는데...
#         if box[i] > box[j]:
#             Falling[box[i]]+=1
#
# print(Falling)
# # max_val = Falling[0]
# # for i in Falling:
# #     if i >= max_val:
# #         max_val = i
# #
# # print("최대 낙차는 : ", max_val)
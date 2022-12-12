def timeMinus(x, y):  # 시간 차이 구하기
    a = int(x[0:2]) - int(y[0:2])
    b = int(x[3:5]) - int(y[3:5])
    return a * 60 + b


def solution(fees, records):
    answer = []
    tmp = {}
    arr = list()
    park = [0] * 10000
    for i in records:
        if i[11:13] == 'IN':  # 출입할 경우 tmp에 차량 번호와 출입 시간 기록
            tmp[i[6:10]] = i[0:5]
        else:  # 출차일 경우 park에 차량 번호 인덱스에 맞게 시간 차이 기록
            park[int(i[6:10])] += timeMinus(i[0:5], tmp[i[6:10]])
            tmp[i[6:10]] = "23:59"

    for j in tmp:  # tmp 에 남아 있는 차량 번호를 정렬하고 출차가 찍히지 않은 차 23:59으로 출차 시킴
        park[int(j)] += timeMinus("23:59", tmp[j])
        arr.append(j)
    arr.sort()

    for k in arr:  # arr에 있는 차량 번호에 맞는 주차 요금 정산해서 answer에 기록
        res = fees[1]
        s = int(park[int(k)])
        s -= fees[0]
        if s > 0:
            if not s % fees[2]:
                s //= fees[2]
                res += s * fees[3]
            else:
                s //= fees[2]
                s += 1
                res += s * fees[3]

        answer.append(res)

    return answer
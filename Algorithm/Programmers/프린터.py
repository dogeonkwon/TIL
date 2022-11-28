def solution(priorities, location):
    if len(priorities) == 1:
        return 1
    n = len(priorities)
    cnt = 1
    left = priorities.pop(0)
    while priorities:
        if location > 0:
            if left < max(priorities):
                priorities.append(left)
            else:
                cnt += 1
            location -= 1
        else:
            if left < max(priorities):
                priorities.append(left)
                location = len(priorities)-1
            else:
                break
        left = priorities.pop(0)


    if not priorities:
        answer = n
    else:
        answer = cnt
    return answer
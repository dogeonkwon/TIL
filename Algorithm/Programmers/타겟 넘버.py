def dfs(arr, k, total):
    global answer

    if k == len(arr):
        if total == tar:
            answer += 1
            return
        else:
            return

    dfs(arr, k + 1, total + arr[k])
    dfs(arr, k + 1, total - arr[k])


def solution(numbers, target):
    global answer, tar
    tar = target
    answer = 0

    dfs(numbers, 0, 0)

    return answer
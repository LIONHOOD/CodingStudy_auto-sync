def solution(arr):
    answer = []
    while arr:
        t = arr.pop()
        if not answer:
            answer.append(t)
        else:
            if answer[-1]!=t:
                answer.append(t)
    return answer[::-1] 
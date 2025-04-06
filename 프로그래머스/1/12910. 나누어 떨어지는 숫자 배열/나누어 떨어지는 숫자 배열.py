def solution(arr, divisor):
    answer = sorted([a for a in arr if a%divisor==0]) or [-1]
    # answer = []
    # for a in arr:
    #     if a%divisor==0:
    #         answer.append(a)
    # answer.sort()
    # if len(answer)==0:
    #     answer.append(-1)
    return answer
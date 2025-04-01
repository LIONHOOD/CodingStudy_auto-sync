def solution(n):
    answer = 0
    for d in range(1,n+1):
        if n%d==0:
            answer += 1
    return answer
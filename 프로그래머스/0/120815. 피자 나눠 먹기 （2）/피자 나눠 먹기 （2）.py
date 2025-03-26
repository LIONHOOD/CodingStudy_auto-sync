def solution(n):
    answer = 1 # n이 6*answer의 약수
    
    while 6*answer%n!=0:
        answer += 1
        
    return answer
def solution(num):
    answer = 0
    while num!=1 and answer<500:
        answer += 1
        if num%2==0:
            num = num//2
        else:
            num = num*3+1
    return [answer, -1][answer==500]
def solution(numbers, target):
    from itertools import product as P
    answer = 0
    for p in P([-1,1], repeat=len(numbers)):
        if sum(s*n for s,n in zip(p,numbers))==target:
            answer += 1
    return answer
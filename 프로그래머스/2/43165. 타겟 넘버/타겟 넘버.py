def solution(numbers, target):
    from itertools import product
    answer = 0 
    for p in product([1,-1], repeat=len(numbers)):
        if target==sum(s*n for s,n in zip(p, numbers)):
            answer += 1
    return answer
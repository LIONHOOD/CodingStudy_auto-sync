def solution(numbers):
    answer = 0
    from itertools import permutations as P
    X = []
    for l in range(1,len(numbers)+1):
        for p in set(P(numbers,l)):
            X.append(int(''.join(p)))
    X = set(X)
    for x in X:
        answer += [0,1][all(x%d for d in range(2,int(x**0.5)+1)) and x>1]
    return answer
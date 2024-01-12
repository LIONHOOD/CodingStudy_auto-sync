def solution(numbers):
    from itertools import permutations as P
    return sum([0,1][all(x%d for d in range(2,int(x**0.5)+1)) and x>1] for x in {int(''.join(p)) for l in range(1,len(numbers)+1) for p in P(numbers,l)})
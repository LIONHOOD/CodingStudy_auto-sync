def solution(clothes):
    from collections import Counter
    from functools import reduce
    T = Counter([c[1] for c in clothes])
    answer = reduce(lambda x,y:x*(y+1), T.values(), 1)-1
    return answer
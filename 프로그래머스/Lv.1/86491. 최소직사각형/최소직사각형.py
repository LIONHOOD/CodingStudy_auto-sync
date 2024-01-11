def solution(sizes):
    m = [(max(s),min(s)) for s in sizes]
    return max(max(m))*max(map(lambda x:x[1], m))
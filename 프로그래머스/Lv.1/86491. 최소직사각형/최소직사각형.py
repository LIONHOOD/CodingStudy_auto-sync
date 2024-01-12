def solution(sizes):
    m = [(max(s),min(s)) for s in sizes]
    return max(m)[0]*max(m, key=lambda x:x[1])[1]
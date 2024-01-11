def solution(priorities, location):
    Q = [(l,p) for l,p in enumerate(priorities)]
    answer = 0
    while True:
        c = Q.pop(0)
        if any(c[1]<q[1] for q in Q):
            Q.append(c)
        else:
            answer += 1
            if c[0]==location:
                return answer
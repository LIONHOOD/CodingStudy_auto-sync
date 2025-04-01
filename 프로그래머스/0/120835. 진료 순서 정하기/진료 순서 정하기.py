def solution(emergency):
    s = sorted(emergency, reverse=True)
    answer = [s.index(e)+1 for e in emergency]
    return answer
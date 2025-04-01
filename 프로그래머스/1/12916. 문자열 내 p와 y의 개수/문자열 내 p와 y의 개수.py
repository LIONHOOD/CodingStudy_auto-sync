def solution(s):
    # answer = s.count('p')+s.count('P')==s.count('y')+s.count('Y')
    s = s.lower()
    answer = s.count('p')==s.count('y')
    return answer
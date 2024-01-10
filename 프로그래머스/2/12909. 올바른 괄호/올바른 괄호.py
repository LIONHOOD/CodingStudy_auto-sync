def solution(s):
    Q = []
    for b in s:
        if b=='(':
            Q.append(b)
        else:
            if not Q:
                return False
            else:
                if Q:
                    Q.pop()
                else:
                    return False
    return False if Q else True
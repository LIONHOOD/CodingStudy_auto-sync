def solution(n, computers):
    N = set(range(n))
    Q = [0]
    S = []
    tmp = []
    while Q:
        c = Q.pop(0)
        tmp.append(c)
        for i in range(n):
            if computers[c][i]==1 and (i not in tmp):
                Q.append(i)
                tmp.append(i)
        if not Q:
            S.append(tmp)
            N -= set(tmp)
            if N:
                Q.append(list(N)[0])
    return len(S)
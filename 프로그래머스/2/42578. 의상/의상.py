def solution(clothes):
    T = {}
    for name,kind in clothes:
        if kind in T:
            T[kind].append(name)
        else:
            T[kind] = [name]
    answer = 1
    for k in T:
        answer *= (len(T[k])+1)
    return answer-1
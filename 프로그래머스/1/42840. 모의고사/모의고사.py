def solution(answers):
    n = len(answers)
    B = [1,2,3,4,5]
    C = [2,1,2,3,2,4,2,5]
    D = [3,3,1,1,2,2,4,4,5,5]
    L = [0]*3
    for a,b,c,d in zip(answers,B*(n//len(B)+1),C*(n//len(C)+1),D*(n//len(D)+1)):
        L[0] += (a==b)
        L[1] += (a==c)
        L[2] += (a==d)
    m = max(L)
    k = L.count(max(L))
    answer = sorted([y for x,y in sorted([*zip(L,[1,2,3])], reverse=True)[:k]])
    return answer
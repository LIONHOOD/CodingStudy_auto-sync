def solution(progresses, speeds):
    import math
    from collections import Counter
    due = [math.ceil((100-p)/s) for p,s in zip(progresses,speeds)]
    for i in range(1,len(due)):
        if due[i-1]>due[i]:
            due[i] = due[i-1]
    return list(Counter(due).values())
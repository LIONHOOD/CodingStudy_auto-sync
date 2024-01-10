def solution(progresses, speeds):
    R = []
    for p,s in zip(progresses, speeds):
        d = -((p-100)//s)
        if not R or R[-1][0]<d:
            R.append([d,1])
        else:
            R[-1][1] += 1
    return [r[1] for r in R]
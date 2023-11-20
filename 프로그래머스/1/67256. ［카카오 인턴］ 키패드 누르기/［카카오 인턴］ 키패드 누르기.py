def solution(numbers, hand):
    l,r = [0,3],[2,3]
    dic = {i+1: [i%3, i//3] for i in range(9)}
    dic[0] = [1,3]
    def dist(c,n):
        return abs(n[0]-c[0]) + abs(n[1]-c[1])
    answer = ''
    for n in numbers:
        if n in [1,4,7]:
            l = dic[n]
            answer += 'L'
        elif n in [3,6,9]:
            r = dic[n]
            answer += 'R'
        else:
            cond = [dist(l,dic[n])<dist(r,dic[n]), dist(l,dic[n])<=dist(r,dic[n])][hand=='left']
            answer += ['R','L'][cond]
            if cond:
                l = dic[n]
            else:
                r = dic[n]
    return answer
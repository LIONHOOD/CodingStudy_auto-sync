import itertools
def solution(users, emoticons):
    answer = [0, 0]
    rate = [10, 20, 30, 40]
    l = len(emoticons)
    for z in itertools.product(rate, repeat=l):
        j, s = 0, 0
        for u in users:
            su = int(sum(emoticons[i]*(100-z[i])/100 for i in range(l) if z[i]>=u[0]))
            if su>=u[1]:
                su = 0
                j += 1
            s += su
        if answer[0]<j:
            answer[0] = j
            answer[1] = s
        elif answer[0]==j and answer[1]<s:
            answer[1] = s
    return answer
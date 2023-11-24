def solution(today, terms, privacies):
    dic = {a:int(m) for a,m in [t.split() for t in terms]}
    answer = []
    for p in range(len(privacies)):
        tmp = int(privacies[p][-7:-5])+dic[privacies[p][-1]]
        y, m = [(tmp//12-1,12), divmod(tmp,12)][bool(tmp%12)]
        exp = str(int(privacies[p][:4]) + y) + ['0'+str(m),str(m)][m//10] + privacies[p][-4:-2]
        if exp<=''.join(today.split('.')):
            answer.append(p+1)
    return answer
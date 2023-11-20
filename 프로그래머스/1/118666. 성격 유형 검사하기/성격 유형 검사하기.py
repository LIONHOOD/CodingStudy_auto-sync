def solution(survey, choices):
    dic = {'R':0,'C':0,'J':0,'A':0}
    for s,c in zip(survey,choices):
        if s[0] in dic.keys():
            dic[s[0]] += 4-c
        else:
            dic[s[1]] += c-4
    return 'RT'[dic['R']<0]+'CF'[dic['C']<0]+'JM'[dic['J']<0]+'AN'[dic['A']<0]
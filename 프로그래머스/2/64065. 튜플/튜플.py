def solution(s):
    s = [set(u.split(',')) for u in s.strip('{}').split('},{')]
    s = sorted(s, key=lambda x: len(x))
    answer = []
    answer.append(int(list(s[0])[0]))
    for i in range(1,len(s)):
        answer.append(int(list(s[i]-s[i-1])[0]))
    return answer
def solution(word):
    P = {a:i for i,a in enumerate('AEIOU')}
    answer = len(word)
    m = [781, 156, 31, 6, 1]
    for i in range(len(word)):
        answer += P[word[i]]*m[i]
    return answer
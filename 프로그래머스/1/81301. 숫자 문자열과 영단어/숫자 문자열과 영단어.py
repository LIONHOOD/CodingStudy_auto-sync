def solution(s):
    for num, word in zip('0123456789', ['zero','one','two','three','four','five','six','seven','eight','nine']):
        s = s.replace(word,num)
        
    return int(s)
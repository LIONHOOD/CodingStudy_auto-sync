def solution(s):
    l = len(s)
    # if l%2==0:
    #     answer = s[l//2-1:l//2+1] 2k-1 = 2(k-1)+1  k-1:k+1
    # else:
    #     answer = s[l//2] k:k+1
    answer = s[(l-1)//2:l//2+1]
    return answer
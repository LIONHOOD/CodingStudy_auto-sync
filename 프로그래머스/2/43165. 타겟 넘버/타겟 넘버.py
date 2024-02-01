answer = 0
def solution(numbers, target):
    n = len(numbers)
    def dfs(c,i):
        global answer 
        if i<n:
            dfs(c+numbers[i],i+1)
            dfs(c-numbers[i],i+1)
        else:
            # global answer
            answer += [0,1][c==target]
            return 
    dfs(0,0)
    return answer
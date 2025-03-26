def solution(n):
    # answer = sum(d for d in range(1,n+1) if n%d==0)
    answer = sum([d for d in range(1,n//2+1) if n%d==0])+n
    # print(help(sum)
    return answer
    # num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
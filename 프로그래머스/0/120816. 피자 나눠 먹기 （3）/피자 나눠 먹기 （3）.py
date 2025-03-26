def solution(slice, n):
    # 총 answer*slice 조각 >= n 명 
    answer = -(-n//slice) 
    return answer
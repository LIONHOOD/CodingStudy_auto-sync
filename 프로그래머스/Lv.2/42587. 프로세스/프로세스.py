# 정답
def solution(priorities, location):
    priorities[location] = str(priorities[location])
    answer = 1
    while len(priorities)>0:
        if isinstance(priorities[0],str):
            tmp = int(priorities[0]) 
        else:
            tmp = priorities[0]
        for p in priorities[1:]:
            if isinstance(p,str):
                p = int(p)
            if tmp<p:
                priorities.append(priorities.pop(0))
                break
        else:
            if isinstance(priorities[0],str):
                return answer
            else:
                priorities.pop(0)
                answer += 1
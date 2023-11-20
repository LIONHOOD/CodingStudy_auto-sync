from functools import reduce
def solution(expression):
    def oper(x,y,op):
        if op=='+': return int(x)+int(y)
        elif op=='-': return int(x)-int(y)
        else: return int(x)*int(y)
    ops = {0: ['+','-','*'],
           1: ['+','*','-'],
           2: ['*','+','-'],
           3: ['*','-','+'],
           4: ['-','+','*'],
           5: ['-','*','+']}
    ans_list = []
    for k in range(6):
        e = expression.split(ops[k][0])
        for i in range(len(e)):
            e[i] = e[i].split(ops[k][1])
            for j in range(len(e[i])):
                e[i][j] = e[i][j].split(ops[k][2])
                e[i][j] = reduce(lambda x,y:oper(x,y,ops[k][2]), e[i][j])
            e[i] = reduce(lambda x,y:oper(x,y,ops[k][1]), e[i])
        e = reduce(lambda x,y:oper(x,y,ops[k][0]), e)
        ans_list.append(abs(e))    
    return max(ans_list)
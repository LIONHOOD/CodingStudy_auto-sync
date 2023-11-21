def solution(places):
    answer = []
    for pl in places:
        pad = ['O'*9]*2 + ['O'*2+r+'O'*2 for r in pl] + ['O'*9]*2
        a = 1
        p = 0
        while a and p<25:
            r, c = p//5+2, p%5+2
            if pad[r][c]=='P':
                if 'P' in [pad[r-1][c],pad[r][c-1],pad[r][c+1],pad[r+1][c]]:
                    a = 0
                    break
                if pad[r-2][c]=='P':
                    if pad[r-1][c]!='X':
                        a = 0
                        break
                if pad[r][c-2]=='P':
                    if pad[r][c-1]!='X':
                        a = 0
                        break
                if pad[r+2][c]=='P':
                    if pad[r+1][c]!='X':
                        a = 0
                        break
                if pad[r][c+2]=='P':
                    if pad[r][c+1]!='X':
                        a = 0
                        break
                if pad[r-1][c-1]=='P':
                    if ['X','X']!=[pad[r-1][c],pad[r][c-1]]:
                        a = 0
                        break
                if pad[r-1][c+1]=='P':
                    if ['X','X']!=[pad[r-1][c],pad[r][c+1]]:
                        a = 0
                        break                    
                if pad[r+1][c-1]=='P':
                    if ['X','X']!=[pad[r+1][c],pad[r][c-1]]:
                        a = 0
                        break
                if pad[r+1][c+1]=='P':
                    if ['X','X']!=[pad[r+1][c],pad[r][c+1]]:
                        a = 0
                        break
            p += 1
        answer.append(a) 
    return answer
def solution(board, moves):
    answer = 0
    box = [None]*1000
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1]!=0:
                if box[-1]==board[i][m-1]:
                    box.pop()
                    answer += 2
                else:
                    box.append(board[i][m-1])
                board[i][m-1] = 0
                break
    return answer
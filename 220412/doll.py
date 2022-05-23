def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        for row in range(len(board)):
            if board[row][move-1] > 0 :
                basket.append(board[row][move-1])
                board[row][move-1] = 0
                
                if basket[-1:] == basket[-2:-1]:
                    answer += 2
                    basket = basket[:-2]
                
                break
    return answer
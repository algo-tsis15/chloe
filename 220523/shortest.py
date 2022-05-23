from collections import deque

def solution(maps):
    answer = 0
    q = deque()
    row, col = len(maps), len(maps[0])
    
    direction = [[1,0], [-1,0], [0,1], [0,-1]]
    board = [[-1 for _ in range(col)] for _ in range(row)]
    
    q.append([0,0])
    board[0][0] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            # 네방향 확인
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            
            # map 내의 범위 
            if (-1 < nx < row) and (-1 < ny < col):
                # 갈 수 있는 길 확인
                if maps[nx][ny] == 1:
                    # 아직 가지 않은 길일 경우
                    if board[nx][ny] == -1:
                        # 간 길로 변경
                        board[nx][ny] = board[x][y] + 1
                        # 말 이동
                        q.append([nx, ny])
                        
    answer = board[-1][-1]
        
    return answer
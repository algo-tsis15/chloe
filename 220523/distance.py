from collections import deque

def bfs(place):
    start = []
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    for i in range(len(place)):
        for j in range(len(place[0])):
            if place[i][j] == 'P':
                start.append([i,j])
    
    for s in start:
        que = deque([s])
        visited = [[0]*5 for _ in range(5)]
        distance = [[0]*5 for _ in range(5)]
        visited[s[0]][s[1]] = 1
        
        while que:
            x, y = que.popleft()
            
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if (0 <= nx < 5) and (0 <= ny < 5) and visited[nx][ny] == 0:
                    if place[nx][ny] == 'O':
                        que.append([nx, ny])
                        visited[nx][ny] = 1
                        distance[nx][ny] = distance[x][y] + 1
                        
                    if place[nx][ny] == 'P' and distance[x][y] <= 1:
                        return 0
    return 1

def solution(places):
    answer = []
    
    for place in places:
        answer.append(bfs(place))
        
    return answer
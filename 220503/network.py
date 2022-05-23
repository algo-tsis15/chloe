from collections import deque

def solution(n, computers):
    answer = 0
    # 초기 세팅
    visited = [0 for i in range(len(computers))]
    
    for i in range(n):
        # 이전에 방문 안했으면
        if not visited[i]:
            # 큐 생성 후 붙이기
            q = deque()
            q.append(i)
            
            while q:
                # i 없애고 방문 표시
                i = q.popleft()
                visited[i] = 1
                
                for j in range(n):
                    # 여기 이해 안됨
                    if computers[i][j] and not visited[j]:
                        q.append(j)
            answer += 1
        
    return answer
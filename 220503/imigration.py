def solution(n, times):
    answer = 0
    
    # 최저, 최고 시간
    left, right = min(times), max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        people = 0
        
        for time in times:
            people += mid // time
            
            # 시간이 충분했던 것으로 간주 -> 줄이기
            if people >= n:
                break
        
        if people >= n:
            answer = mid
            right = mid - 1
        # 시간이 부족했던 것으로 간주 -> 늘리기
        elif people < n:
            left = mid + 1
    
    return answer
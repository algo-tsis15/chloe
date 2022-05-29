def solution(n, lost, reserve):
    answer = n # 반환값 초기 세팅
    
    new_lost = set(lost) - set(reserve) # 중복 제거
    new_reserve = set(reserve) - set(lost)
    
    for item in new_reserve:
        if (item - 1) in new_lost: # 여분을 분배 받을 수 있는 경우 list에서 제거 
            new_lost.remove(item-1)
        elif (item + 1) in new_lost:
            new_lost.remove(item+1)
    
    return answer - len(new_lost) # 여분을 분배 받지 못한 경우의 학생들을 초기값에서 빼줌
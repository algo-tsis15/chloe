def solution(numbers, target):
    answer = 0
    answers = [0]
    
    for n in numbers:
        tmp = [] 
        for ans in answers:
            # 더하기, 빼기 경우에 따라 가지 뻗기
            tmp.append(ans - n)
            tmp.append(ans + n)
        answers = tmp
    
    for ans in answers:
        if ans == target:
            answer += 1
            
    return answer


"""
from itertools import product

def solution(numbers, target):
    tmp = [(n, -n) for n in numbers]
    answer = list(map(sum, product(*tmp)))

    return answer.count(target)
"""
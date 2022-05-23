from itertools import combinations

def solution(relation): 
    answer = 0
    
    candidate = []
    for i in range(1, len(relation)):
        for r in combinations(relation, i):
            if r in candidate: break
            else: candidate.extend(r) # check duplication
        
        
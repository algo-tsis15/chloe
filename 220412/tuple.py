def solution(s):
    tmp = []
    answer = []
    
    for i in sorted(s[1:-1].split("},"), key=len):
        tmp.append(i.replace("{","").replace("}","").split(","))
    
    for i in tmp: 
        for j in list(map(int,i)):
            if j not in answer:
                answer.append(j)
    
    return answer
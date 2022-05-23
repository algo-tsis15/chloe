def solution(record):
    answer = []
    dic = {}
    count = {}
    cnt = 1
    
    for i in range(len(record)):
        tmp = record[i].split(" ")
        if tmp[1] not in dic:
            dic[tmp[1]] = {tmp[2] : [tmp[0]]}
            count[cnt] = tmp[1]
            cnt += 1
        else:
            if tmp[0] != 'Change': 
                count[cnt] = tmp[1]    
                cnt += 1
            for key in dic[tmp[1]].keys():
                if tmp[0] == 'Leave':
                    dic[tmp[1]][key] += [tmp[0]]
                elif tmp[0] == 'Enter':
                    if tmp[2] != key:
                        dic[tmp[1]] = {tmp[2] : dic[tmp[1]][key] + [tmp[0]]}
                    else :
                        dic[tmp[1]][key] += [tmp[0]]
                else:
                    dic[tmp[1]] = {tmp[2] : dic[tmp[1]][key]}
                    
    for i in count.keys():
        for key in dic[count[i]].keys():
            if(len(dic[count[i]][key]) != 0) :
                if dic[count[i]][key].pop(0) == 'Enter':
                    answer.append(key + "님이 들어왔습니다.")
                else :
                    answer.append(key + "님이 나갔습니다.")
        
    return answer
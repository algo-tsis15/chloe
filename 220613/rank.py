from collections import defaultdict
from itertools import combinations as cb
import bisect

def solution(info, query):
    query = [i.replace('and ','').split() for i in query]
    info = [i.split() for i in info]

    info_dic = defaultdict(list)

    for language, job, carrer, food, score in info:
        for i in range(5):
            for j in cb([language, job, carrer, food],i):
                info_dic[''.join(j)].append(int(score))

    for i in info_dic:
        info_dic[i].sort()

    answer = []
    for i in query:

        score = int(i[-1])
        result = ''.join(i[:-1]).replace('-','')
        s = info_dic[result]
        answer.append(len(s) - bisect.bisect_left(s,score))

    return answer
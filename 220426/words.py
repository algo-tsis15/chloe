def solution(begin, target, words):
    answer = 0
    stack = [begin]
    
    if target not in words:
        return 0
    
    while words:
        tmp = []
        for w in stack:
            for word in words: # every item in stack compares with the word from words
                diff = 0
                for i in range(len(word)):
                    if word[i] != w[i]:
                        diff += 1
                    if diff > 1:
                        break
                if diff == 1:
                    tmp.append(word) # save closest item
                    words.remove(word) # remove used item
        answer += 1
        if target in tmp: return answer
        else: stack = tmp
    
    return answer
    
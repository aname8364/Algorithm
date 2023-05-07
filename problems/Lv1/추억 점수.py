def solution(name, yearning, photo):
    answer = [0] * len(photo)
    d = {}
    
    for i,v in enumerate(yearning):
        d[name[i]] = v 
    
    for i,p in enumerate(photo):
        for j in p:
            if j in d:
                answer[i] = answer[i] + d[j]
            
    return answer
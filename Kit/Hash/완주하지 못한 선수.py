def solution(participant, completion):
    #hash = {name: 0 for name in participant}
    hash = {}
    for name in participant:
        if not name in hash:
            hash[name] = 0
        hash[name] = hash[name] + 1 
        
    for name in completion:
        hash[name] = hash[name] - 1
    
    return list(hash.keys())[list(hash.values()).index(1)]
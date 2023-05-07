def solution(arr):
    answer = []
    for i,v in enumerate(arr):
        if i == 0:
            answer.append(v)
        else:
            if answer[-1] != v:
                answer.append(v)
            
    return answer
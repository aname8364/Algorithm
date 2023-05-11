
def solution(n, m, section):
    count = 0
    last_painted = -1
    for i in section:
        if i > last_painted:
            last_painted = i+m-1
            count = count + 1
    answer = count
    return answer

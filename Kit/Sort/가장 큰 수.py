def solution(numbers):
    answer = ''
    temp = sorted(numbers, key=lambda x: str(x)*3, reverse=True)
    for i in temp:
        answer = answer + str(i)
    answer = str(int(answer))
    return answer
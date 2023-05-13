def solution(array, commands):
    answer = []
    for command in commands:
        temp = array[command[0]-1:command[1]]
        n = sorted(temp)[command[2]-1]
        answer.append(n)
          
    return answer
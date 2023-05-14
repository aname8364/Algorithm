def solution(cards1, cards2, goal):
    answer = "No"
    count_to_find = len(goal)
    current_count = 0
    
    for text in goal:
        if len(cards1) > 0 and cards1[0] == text:
                cards1.pop(0)
                current_count = current_count + 1

        elif len(cards2) > 0 and cards2[0] == text:
                cards2.pop(0)
                current_count = current_count + 1

    if current_count == count_to_find:
        answer = "Yes"

                
    return answer

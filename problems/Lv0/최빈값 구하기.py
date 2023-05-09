from collections import Counter

def solution(array):
    if len(array) == 1:
        return array[0]
    temp = Counter(array).most_common()
    if len(temp) == 1:
        return temp[0][0]
    if temp[0][1] == temp[1][1]:
        return -1
    return temp[0][0]
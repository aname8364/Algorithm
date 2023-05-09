def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif stack and c == ")" and stack[len(stack)-1] == "(":
            stack.pop()
        else:
            return False
    return len(stack) == 0

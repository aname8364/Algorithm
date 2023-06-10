def check(ps):
    stack = []
    for c in ps:
        if c == '(':
            stack.append(c)
        elif c == ')' and stack and stack[-1] == "(":
            stack.pop()
        else:
            return False
    return len(stack) == 0

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(str, input().split())))

for s in arr:
    print(check(*s) and "YES" or "NO")

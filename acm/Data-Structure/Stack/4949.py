def check(ps):
    z = []
    for c in s:
        if c == '(' or c == '[':
            z.append(c)
        elif c == ')':
            if z and z[-1] == '(':
                z.pop()
            else:
                return False
        elif c == ']':
            if z and z[-1] == '[':
                z.pop()
            else:
                return False
    return len(z)==0

while True:
    s = input()
    if s == '.':
        break
    print(check(s) and "yes" or "no")
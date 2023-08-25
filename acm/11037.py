def f(k):
    x = []
    for i in range(k+1, 1000000000):
        e = str(i)
        g = True
        if e.count('0') > 0:
            g = False
        for j in range(1, 10):
            if e.count(str(j)) > 1:
                g = False
                break
        if g:
            x.append(g)
            return i
    return 0

while True:
    try:
        n = int(input())
        print(f(n))
    except:
        break
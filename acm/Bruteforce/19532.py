" PyPy3 "

a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        c1 = (a*x) + (b*y)
        c2 = (d*x) + (e*y)
        if c1 == c and c2 == f:
            print(x,y)
            break


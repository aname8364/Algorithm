import math
    
n = int(input())
for _ in range(n):
    m = int(input())
    y = math.floor(math.log2(m))
    b = m-(2**y)
    if b == 0:
        x = y-1
        y = x
    else:
        x = math.floor(math.log2(b))
    print(x, y)
p = map(int, input().split())
x, y, r = map(int, input().split())
b = False

for i,v in enumerate(p):
    
    if v==x:
        print(i+1)
        b = True
        break
    
if not b:
    print(0)
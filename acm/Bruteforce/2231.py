n = int(input())
found = False
for i in range(1, n-1):
    x = i
    for c in str(i):
        x += int(c) 
    if x == n:
        print(i)
        found = True
        break
    
if not found:
    print(0)
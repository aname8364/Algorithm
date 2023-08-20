n = int(input())

x: list = [-1 for i in range(5000+1)]

x[3] = 1
x[5] = 1

for i in range(6, n+1):
    v = x[i]
    a, b = x[i], x[i]
    if x[i-5] != -1 and x[i-3] != -1:
        x[i] = min(x[i-5]+1, x[i-3]+1)
    elif x[i-5] != -1 and x[i-3] == -1:
        x[i] = x[i-5] +1
    elif x[i-5] == -1 and x[i-3] != -1:
        x[i] = x[i-3] +1
        
print(x[n])
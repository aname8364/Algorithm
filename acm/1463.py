n = int(input())

e = [0 for i in range(1000001)]

e[1] = 0
e[2] = 1
e[3] = 1

for i in range(4, n+1):
    v = [123456, 123456, 123456]
    if i%3==0:
        v[0] = e[i//3] + 1
    if i%2==0:
        v[1] = e[i//2] + 1
    v[2] = e[i-1] + 1
    e[i] = min(v)
        
print(e[n])
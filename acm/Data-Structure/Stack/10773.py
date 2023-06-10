x = int(input())
data = []
for _ in range(x):
    data.append(list(map(str, input().split())))

y = []
for n in data:
    m = int(*n)
    if m == 0:
        y.pop()
    else:
        y.append(m)
print(sum(y))
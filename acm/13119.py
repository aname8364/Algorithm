h, w, y = map(int, input().split())

"""
.....#....
....##....
....##....
----**-*--
.#|.##.#|.
.#|###.##.
.########.
#########.
"""
x = [['.' for _ in range(w)] for _ in range(h)]

for i in range(w):
    x[h-y][i] = '-'
    
n = map(int, input().split())
for i,m in enumerate(n):
    for j in range(h-1, h-m-1, -1):
        if x[j][i] == '-':
            x[j][i] = '*'
        else:
            x[j][i] = '#'
            
    if (i+1)%3==0 and i!=0:
        for j in range(h-y+1, h):
            if x[j][i] == '.':
                x[j][i] = '|'


for i in x:
    print(''.join(i))
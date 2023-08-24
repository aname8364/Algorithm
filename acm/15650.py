import itertools

n, m = map(int, input().split())
x = [i for i in range(1, n+1)]

v = list(itertools.combinations(x, m))

for i in v:
    print(*i)
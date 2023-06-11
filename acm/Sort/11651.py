x = int(input())
p = [list(map(int, input().split())) for i in range(x)]
t = sorted(p, key=lambda t: (t[1], t[0]))
print(*[f"{z[0]} {z[1]}" for z in t], sep="\n")
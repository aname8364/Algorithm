n = int(input())
users = [0 for _ in range(n)]

for i in range(n):
    users[i] = input().split()

v = sorted(users, key=lambda x: int(x[0]))
for x in v:
    print(x[0], x[1])
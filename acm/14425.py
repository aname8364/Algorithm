n, m = map(int, input().split())

# s d

strings = {}
for i in range(n):
    string = input()
    strings[string] = True
    
count = 0

for i in range(m):
    string = input()
    if string in strings:
        count += 1

print(count)
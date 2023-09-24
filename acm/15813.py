n = int(input())
s = input()

x = 0
for c in s:
    x += ord(c)-64
    
print(x)
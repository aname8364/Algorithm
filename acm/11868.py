n = int(input())

v = list(map(int, input().split()))

x = 0

for i in v:
    x ^= i
    
if x:
    print("koosaga")
else:
    print("cubelover")
arr = [[0 for i in range(200+1)] for i in range(200+1)]

n, k = map(int, input().split())

for i in range(n+1):
    arr[1][i] = 1
    
for i in range(k+1):
    arr[i][1] = i
    
for i in range(2, k+1):
    for j in range(2, n+1):
        arr[i][j] = (arr[i-1][j] + arr[i][j-1]) % 1000000000

print(arr[k][n])

# 15 days ago
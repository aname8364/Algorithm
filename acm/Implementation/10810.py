n, m = map(int, input().split())
arr = [0 for i in range(n)] # n개의 바구니

for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i, j+1):
        arr[x-1] = k # i 부터 j 번까지의 바구니 = k
        
print(*arr)
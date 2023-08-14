import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num_arr = list(map(int, input().split()))

sum_arr = [0] * (n+1)
fix_arr = [0] * (n+1)

for i in range(n):
    sum_arr[i+1] = sum_arr[i] + num_arr[i]
    fix_arr[i+1] = sum_arr[i+1] - sum_arr[i-(k-1)]

print(max(fix_arr[k:]))
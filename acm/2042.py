import sys
input = sys.stdin.readline

def merge(left, right):
    return left+right
    
def build(tree, node, left, right):
    if left == right:
        tree[node] = x[left]
        return tree[node]
    
    mid = (left+right)//2
    left_val = build(tree, node*2, left, mid)
    right_val = build(tree, node*2+1, mid+1, right)
    tree[node] = merge(left_val, right_val)
    return tree[node]
    
def query(tree, start, end, node, left, right):
    if left>end or right<start:
        return 0
        
    if left>=start and right<=end:
        return tree[node]
        
    mid = (left+right)//2
    left_val = query(tree, start, end, node*2, left, mid)
    right_val = query(tree, start, end, node*2+1, mid+1, right)
    return merge(left_val, right_val)
        
def update(tree, idx, value, node, left, right):
    if idx<left or idx>right:
        return tree[node]
        
    if left == right:
        tree[node] = value
        return tree[node]
        
    mid = (left+right)//2
    left_val = update(tree, idx, value, node*2, left, mid)
    right_val = update(tree, idx, value, node*2+1, mid+1, right)
    tree[node] = merge(left_val, right_val)
    return tree[node]
    
n, m, k = map(int, input().split())

x = []
for i in range(n):
    x.append(int(input()))
    
t = [0] * (4 * n)

build(t, 1, 0, n-1)

for i in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(t, b-1, c, 1, 0, n-1)
    else:
        z = query(t, b-1, c-1, 1, 0, n-1)
        print(z)
        
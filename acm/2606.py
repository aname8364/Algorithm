pc = {}

pc_count = int(input())
connected_count = int(input())

#     s  d

def dfs(g, r) -> list:
    visited = []
    stack = [r]
    
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in pc:
                stack += list(set(g[n]) - set(visited))
    return visited
    

for i in range(connected_count):
    pc_1, pc_2 = map(int, input().split())
    if pc_1 not in pc:
        pc[pc_1] = []
    pc[pc_1].append(pc_2)
        
    if pc_2 not in pc:
        pc[pc_2] = []
    pc[pc_2].append(pc_1)

print(len(dfs(pc, 1))-1)
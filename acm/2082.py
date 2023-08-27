h1 = [[0,0,0] for i in range(5)]
h2 = [[0,0,0] for i in range(5)]
m1 = [[0,0,0] for i in range(5)]
m2 = [[0,0,0] for i in range(5)]

for i in range(5):
    c = input().split()
    
    h1[i] = c[0]
    h2[i] = c[1]
    m1[i] = c[2]
    m2[i] = c[3]
    
num = {
    "0": [
        [1,1], [2,1], [3,1]
    ],
    "1": [
        [0,0], [0,1], [1,0], [1,1], [2,0], [2,1], [3,0], [3,1], [4,0], [4,1]
    ],
    "2": [
        [1,0], [1,1], [3,1], [3,2]
    ],
    "3": [
        [1,0], [1,1], [3,0], [3,1]
    ],
    "4": [
        [0,1], [1,1], [3,0], [3,1], [4,0], [4,1]  
    ],
    "5": [
        [1,1], [1,2], [3,0], [3,1]
    ],
    "6": [
        [1,1], [1,2], [3,1]  
    ],
    "7": [
        [1,0], [1,1], [2,0], [2,1], [3,0], [3,1], [4,0], [4,1]
    ],
    "8": [
        [1,1], [3,1]
    ],
    "9": [
        [1,1], [3,0], [3,1]
    ]
}

def get_num(arr):
    for i in range(10):
        found = True
        for j in num[str(i)]:
            x, y = j[1], j[0]
            if arr[y][x] == "#":
                found = False
                continue
        if found:
            return i
        
print(f"{get_num(h1)}{get_num(h2)}:{get_num(m1)}{get_num(m2)}")
        
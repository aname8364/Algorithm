r, c = map(int, input().split())

arr = []
wolf = []

sheep_count = 0

for i in range(r):
    arr.append(input())
    arr[i] = arr[i].replace(".", "D")
    wolf.append([pos for pos, char in enumerate(arr[i]) if char == "W"])
    wolf[i].append(i)
    
    sheep_count += arr[i].count("S")

can_block = True

def check_left(x, y):
    return arr[y][x-1] == "S"
    
def check_right(x, y):
    return arr[y][x+1] == "S"
    
def check_up(x, y):
    return arr[y-1][x] == "S"
    
def check_down(x, y):
    return arr[y+1][x] == "S"

for w in wolf:
    y = w[-1]
    pos = w[:-1]
    for x in pos:
        check_array = []
        
        if x>0:
            check_array.append(check_left(x, y))
        if x<c-1:
            check_array.append(check_right(x, y))
        if y>0:
            check_array.append(check_up(x, y))
        if y<r-1:
            check_array.append(check_down(x, y))
            
        for i in check_array:
            if i:
                can_block = False
                break
        
        
        
if sheep_count == 0:
    can_block = True
        
if can_block:
    print(1)
    for i in arr:
        print(''.join(i))
else:
    print(0)
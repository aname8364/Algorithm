room_number = input()

inven: dict = {i: 0 for i in range(10)}

buy_count: int = 0

def buy_one():
    global buy_count
    for i in range(10):
        inven[i] += 1
    buy_count += 1
    
def is_empty(n) -> bool:
    return inven[n] <= 0


for c in room_number:
    num = int(c)
    if num in [6, 9]:
        other_num = 9 if num == 6 else 6
        if is_empty(num) and is_empty(other_num):
            buy_one()
            inven[num] -= 1
        elif not is_empty(other_num):
            inven[other_num] -= 1
        else:
            inven[num] -= 1
    else:
        if is_empty(num):
            buy_one()
        inven[num] -= 1
        

print(buy_count)

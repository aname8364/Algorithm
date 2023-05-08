DEBUG = True

def log(name, text):
    if DEBUG:
        print(f"{name}: {text}")

def solution(park, routes):

    # 맵 넘어가는지 확인용
    MAP_WIDTH = len(park[0])
    MAP_HEIGHT = len(park)

    def is_blocked(x, y):
        # 맵보다 멀리 감
        if x >= MAP_WIDTH or y >= MAP_HEIGHT:
            return True
        
        if x < 0 or y < 0:
            return True
        
        # 벽 있음
        if park[y][x] == "X":
            return True
        
        return False
    
    # 이동시 is_blocked에 걸리면,
    # 움직인 거리 초기화

    def move_x(pos, x):
        log("move_x", f"{pos} {x}")
        new_pos = list(pos)
        step = (1) if x>0 else (-1)
        for i in range(pos[0]+step, pos[0]+x+step, step):
            # 1, 3, 1  -> 2, 4, 1  -> 2 3
            # 3, 1, -1 -> 2, 0, -1 -> 2, 1
            if not is_blocked(i, pos[1]):
                log("x_blocked", f"false {i}")
                pos[0] = pos[0] + step
                log("move_x_step", f"{pos}")
            else:
                log("x_blocked", f"true {i}")
                pos = new_pos
                break
        log("move_x_end", f"{pos}")
        return pos

    def move_y(pos, y):
        log("move_y", f"{pos} {y}")
        new_pos = list(pos)
        step = (1) if y>0 else (-1)
        for i in range(pos[1]+step, pos[1]+y+step, step):
            if not is_blocked(pos[0], i):
                log("y_blocked", f"false {i}")
                pos[1] = pos[1] + step
                log("move_y_step", f"{pos}")
            else:
                log("y_blocked", f"true {i}")
                pos = new_pos
                break
        return pos



    answer = []
    start = 0        # S 시작 위치
    mypos = [0, 0]   # 내 현재 위치


    # 스폰 위치 설정
    for i,v in enumerate(park):
        start = v.find("S")     # 맵에서 S 찾기
        if start != -1:         # 찾음
            mypos = [start, i]  # 내 위치 시작위치로 설정
            break

    # 이동
    for i in routes:
        op = i[0]
        n  = int(i[2])

        if op == "N":
            mypos = move_y(mypos, -n)
        
        elif op == "S":
            mypos = move_y(mypos, n)

        elif op == "W":
            mypos = move_x(mypos, -n)

        elif op == "E":
            mypos = move_x(mypos, n)

    answer = [mypos[1], mypos[0]]
    return answer




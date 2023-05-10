def solution(wallpaper):
    start_point = [999, 999]
    end_point = [-1, -1]
    for i, tiles in enumerate(wallpaper):
        for j, tile in enumerate(tiles):
            if tile == "#":
                if i < start_point[0]:
                    start_point[0] = i
                if j < start_point[1]:
                    start_point[1] = j
                
                if i+1 > end_point[0]:
                    end_point[0] = i+1
                if j+1 > end_point[1]:
                    end_point[1] = j+1
                    
    answer = [start_point[0], start_point[1], end_point[0], end_point[1]]
    return answer
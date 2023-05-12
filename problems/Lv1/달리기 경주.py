def solution(players, callings):
    answer = []

    plist = {player: index for index, player in enumerate(players)}

    for player in callings:
        i = plist[player]
        j = i - 1
        players[i], players[j] = players[j], players[i]
        plist[players[i]], plist[players[j]] = i, j
    answer = players

    return answer
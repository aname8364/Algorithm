def solution(keymap, targets):
    answer = [0 for i in range(len(targets))]
    for i, target in enumerate(targets):
        for c in target:
            min_click = 999
            not_found = True
            for key in keymap:
                idx = key.find(c)
                if idx != -1:
                    # 해당 key 로 누를 수 있음
                    # 가장 클릭 횟수가 적은 경우로 선택
                    # [0]에 있으면 1번 클릭
                    min_click = min(min_click, idx+1)
                    not_found = False
                    
            # 못 누르는 경우
            # -1로 설정
            if not_found:
                answer[i] = -1
                break
                
            answer[i] = answer[i] + min_click
    return answer
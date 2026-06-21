import math

def solution(signals):
    
    # 시그널들의 싸이클을 찾아야함

    cycle_lst = []
    for lst in signals:
        cycle_lst.append(sum(lst))
    
    # 실제 시간 -> 1은 무조건 초록불임으로 답이 될 수 없음. 2부터 시작
    time = 2

    # 싸이클의 최소공배수까지 반복해도 안되면 멈춰야함
    lcm = math.lcm(*cycle_lst)

    while time <= lcm:

        all_yellow = True

        # 시그널들을 하나씩 순회하면서 yellow 인지 확인
        for i, lst in enumerate(signals):
            
            # 변환된 시간 = 실제시간을 싸이클만큼 나눈 나머지
            adjusted_time = (time - 1) % cycle_lst[i] + 1

            # 옐로우 타임이 아니라면 break
            green_time = lst[0]
            yellow_time = lst[0] + lst[1]

            if not green_time < adjusted_time <= yellow_time:
                all_yellow = False
                break
        
        # 전부 통과 시 결과 반환
        if all_yellow:
            return time
        
        # for문이 조건 불만족으로 break되면 시간 + 1
        time += 1
    
    return -1

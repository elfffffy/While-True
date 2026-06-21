def solution(schedules, timelogs, startday):

    # 정답
    total_cnt = 0

    # 직원의 수
    employee_cnt = len(schedules)

    # 직원 별로 순회 체크
    for i in range(employee_cnt):
        
        # 해당 직원이 설정한 목표 시간
        set_time = schedules[i]

        # 해당 직원의 제한 시간
        goal_time = set_time + 10

        # 분 단위가 60이 넘으면, 시간을 적절하게 수정
        if goal_time % 100 >= 60:
            goal_time += (100 - 60)


        # 일주일을 순회
        for j in range(7):
            
            # 그 날의 요일 -> 1을 빼고 다시 더해야, 7 % 7 = 0이 되지 않게 할 수 있음
            day_of_the_week = (startday + j - 1) % 7 + 1

            # 토요일, 일요일은 해당 없음
            if day_of_the_week == 6 or day_of_the_week == 7: continue

            # 출근 시간이 목표 시간을 지났으면 상품 자격 X
            if timelogs[i][j] > goal_time: break

        # 모든 조건 다 통과 시,
        else:
            total_cnt += 1
    
    return total_cnt
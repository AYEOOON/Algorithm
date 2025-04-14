"""
1. 출근 인정 시간 계산
  - 각 직원의 출근 희망 시각 + 10분을 계산하여, 출근 마감 시각(인정 시각)으로 설정
2. 요일 순환 처리
  - 시작 요일(startday)부터 7일 동안의 요일을 계산하며, 토요일(6)과 일요일(7)은 무시
3. 출근 시간 비교
  - 매일의 출근 로그 중 평일만 확인하여, 출근 시간이 인정 시각 이하면 통과로 간주
4. 5일 모두 정시에 출근했는지 체크
  - 평일 5일 모두 늦지 않고 출근했으면 해당 직원은 상품을 받게 됨
5. 상품 받을 직원 수 집계
  - 조건을 만족한 직원 수를 최종 결과로 리턴
"""

# 출근 희망 시각(n명), 일주일 동안 출근한 시각, 요일(startday 기준, 토요일(6), 일요일(7)은 제외)
def solution(schedules, timelogs, startday):
    answer = 0  # 상품을 받을 직원 수를 저장할 변수 초기화
    weekdays = {1, 2, 3, 4, 5}  # 평일(월~금)을 나타내는 집합, 포함 여부 검사(in 연산) 목적이라면 set이 더 효율적이다.

    # 모든 직원에 대해 반복
    for i in range(len(timelogs)):
        # 출근 희망 시각을 시(hour)와 분(minute)로 분리
        hour = schedules[i] // 100
        minute = schedules[i] % 100 + 10  # 희망 시각 + 10분

        # 분이 60 이상이면 시(hour)를 증가시키고 분을 조정
        if minute >= 60:
            hour += 1
            minute -= 60

        # 최종적으로 허용되는 출근 시각을 계산 (정수로 시*100 + 분)
        allow_time = hour * 100 + minute
        
        # 출근 요일을 시작 요일로 설정
        day = startday
        okay = 0  # 정시에 출근한 평일 수

        # 7일 동안의 출근 기록 확인
        for log in timelogs[i]:
            # 현재 요일이 평일인 경우만 검사
            if day % 7 in weekdays:
                # 출근 시간이 허용된 시간 이내면 인정
                if log <= allow_time:
                    okay += 1
            day += 1  # 다음 날로 이동

        # 평일 5일 모두 정시에 출근했으면 상품 대상
        if okay == 5:
            answer += 1

    return answer  # 상품을 받을 직원 수 반환

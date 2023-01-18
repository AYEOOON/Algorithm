# 각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다.
# 각 angle이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성하는 문제.


# 내 풀이

def solution(angle):
    if angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90<angle and angle<180:
        return 3
    else:
        return 4
      
      
# 다른사람 풀이

def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer

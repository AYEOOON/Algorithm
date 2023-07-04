# 삼각형을 만드려면, 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야하는 조건을 만족하면1, 아니면 2를 반환하는 문제

# 내 풀이

def solution(sides):
    sides.sort()
    if sides[0]+sides[1] > sides[2]:
        return 1
    else:
        return 2
      
      
# 다른사람 풀이

def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2

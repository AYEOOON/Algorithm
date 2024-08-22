"""
코니는 매일 다른 옷을 조합하여 입는것을 좋아합니다.

  - 코니는 각 종류별로 최대 1가지 의상만 착용할 수 있습니다. 
  - 착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법으로 옷을 착용한 것으로 계산합니다.
  - 코니는 하루에 최소 한 개의 의상은 입습니다.

코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.
"""

# 2차원 배열의 [옷, 종류]를 딕셔너리로 초기화
# 각 종류의 옷이 나올 때 마다 +1
# a*b*c = abc로 조합가능한 모든 경우의 수, 하지만 안입는 경우도 존재하기 때문에 각각 +1을 해줌, 하지만 abc 전부 안입는 경우는 제외해야 하므로 -1

# 내 풀이
def solution(clothes):
    closet = {clothes[i][1]:0 for i in range(len(clothes))}
    
    for i in range(len(clothes)):
        closet[clothes[i][1]] += 1
        
    cnt = 1
    
    for key, value in closet.items():
        cnt *= (value+1)
        
    return cnt-1


# 다른사람 풀이
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1 # reduce : 여러 개의 데이터를 대상으로 주로 누적 집계를 내기위해 사용
    return answer

# 영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.

# 내 풀이

import numpy

def solution(score):
    answer = []
    arr = []
    for i in score:
        arr.append(numpy.mean(i))     # score의 평균을 구해 arr리스트에 append()
        
    sort_arr = sorted(arr,reverse = True)  # 정렬한 새로운 리스트를 반환하는 sorted()함수를 이용하여 arr리스트를 정렬한 후 sort_arr에 저장
        
    for j in arr:
        answer.append(sort_arr.index(j)+1) # score의 평균을 저장한 의 순위를 알 수 있도록 정렬한 sort_arr에서 해당 score의 요소를 찾아 answer 리스트에 apppend()한다.

    
    return answer

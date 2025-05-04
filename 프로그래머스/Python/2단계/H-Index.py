"""
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 
어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 
이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.
"""
"""
 1. 배열을 내림차순 정렬한다. 
 2. f가 현재 위치의 값보다 크거나 작은 곳의 위치를 기록
 3. 거기서 다시 탐색
"""

# 내 풀이
def solution(citations):
    f = 0
    h = len(citations)
    i = 0
    
    citations.sort(reverse = True)
    
    while(True):
        if f == len(citations):
            break
        
        if citations[i] > f:
            f += 1
    
        else:
            h = f
            break
        i += 1
    
    return h


# 다른사람 풀이 1
# enumrate로 (index, value)형태로 묶는다. 
# 그리고 최댓값(start=1)부터 각 value에 대해 최솟값 value의 값을 min으로 추출
# 이 추출된 값은 enumerate가 끝나는 citations 리스트의 크기에 해당하는 갯수가 나옴.
# 이들을 map으로 묶으면, 한 value의 입장에서 보는 최솟값 value의 집합이 나옴
# 즉, h값들의 집합이 나온다. h값 중 최댓값을 max로 뽑아서 출력

#  1) min(index,value) 부분은 가능할 수 있는 모든 h-index를 추출하는 부분 
# 2) max(~) 값은 가능할 수 있는 모든 h-index 중 가장 큰 값을 추출하는 부분

def solution(citations):
    citations.sort(reverse=True)  # 배열 내림차순 정렬
    answer = max(map(min, enumerate(citations, start=1)))  
    return answer
  

# 다른사람 풀이 2
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

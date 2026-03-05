'''
https://school.programmers.co.kr/learn/courses/30/lessons/67258
: 보석 매장에 진열된 보석 목록 gem이 주어지면, 모든 종류의 보석을 최소 1개 이상 포함하는 가장 짧은 구간을 찾는 문제

처음에는 모든 시작점에서 끝가지 탐색하는 브루트포스 방식을 생각할 수 있다.
하지만 gems의 최대 길이가 100,000이기 때문에 O(N^2)이 된다. 따라서 효율성 테스트에 통과할 수 없는 문제가 있다.

따라서 투 포인터와 슬라이딩 윈도우 기법을 사용하여 해결한다. 

[핵심 아이디어]
1. 두 개의 포인터 start, end를 사용하여 구간을 관리한다. 
2. end를 이동시키며 보석을 window에 추가한다. 
3. 현재 구간이 모든 보석 종류를 포함하면
  - start를 이동시키며 구간을 최소화환다. 
4. 그 과정에서 가장 짧은 구간을 갱신한다. 

[배운 점]
- 슬라이딩 윈도우 패턴을 사용하면 구간 문제를 효율적으로 해결할 수 있다.
- 특정 조건을 만족하는 최소 구간 문제는 투 포인터로 해결되는 경우가 많다.
- HashMap을 이용해 현재 윈도우 상태를 관리하는 방식이 중요하다.
'''

from collections import defaultdict

def solution(gems):
    types = len(set(gems))  # 전체 보석 종류 수 (문제에서 요구하는 것은 모든 종류를 포함하는 구간이므로 갯수를 먼저 계산한다.)
    start = 0
    counter = defaultdict(int)  # 현재 구간에 포함된 보석 개수 관리
    answer = [start, len(gems)-1]
    
    for end in range(len(gems)):  # end 확장
        counter[gems[end]] += 1 # 보석 갯수 추가
        
        while(len(counter) == types): # 현재 윈도우가 모든 보석을 포함한 상태
            
            if end - start < answer[1] - answer[0]: # 최소 구간 갱신
                answer = [start, end]
                
            counter[gems[start]] -= 1 # start 보석 제거
            
            if counter[gems[start]] == 0: # 보석 개수가 0이 되면 dict에서 삭제
                del counter[gems[start]]
            
            start += 1 # 왼쪽 포인터 이동
        
    return [answer[0]+1, answer[1]+1]

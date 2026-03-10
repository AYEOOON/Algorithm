'''
https://school.programmers.co.kr/learn/courses/30/lessons/12927
: 아근 피로도는 각 작업량^2 의 합으로 계산된다. 작업량이 담긴 배열 works와 남은 시간 n이 주어질 때 야근 피로도의 최소값을 구하는 문제

작업량이 큰 값을 줄이는 것이 피로도 감소에 큰 영향을 준다. 

처음에는 단순히 정렬을 반복하는 방식으로 접근을 했지만, 효율설 테스트에서 실패했다.
정답 로직은 맞았지만 코드의 반복 구조가 매번 works 배열을 정렬하기 때문에 O(W log W)가 n번 반복하다보니 통과가 불가능한 것이었다.

정렬은 너무 무거운 작업이기 때문에 가장 큰 값을 빠르게 꺼낼 수 있는 자료 구조인 힙을 사용했다.
파이썬의 기본 힙은 최소 힙이기 때문에 모든 배열 값을 음수로 저장한다.

[알고리즘]
1. works를 heap에 넣는다. 
2. n번 반복한다.
  - 가장 큰 값 pop
  - 1 줄이기
  - 다시 push 
'''

import heapq

def solution(n, works):
    answer = 0
    heap = []
    for work in works:
        heapq.heappush(heap,work*(-1))

    if sum(works) <= n:
        return answer
    
    while n > 0:
        tmp = heapq.heappop(heap)
        heapq.heappush(heap, tmp+1)
        n -= 1
        
    for i in heap:
        answer += i*i
    
    return answer

'''
[다른 사람의 풀이]
내 풀이는 heappush 반복해서 힙으로 만들었지만, 다른 풀이는 heapify를 사용해서 O(N) 시간에 힙을 생성하였다.
- heapify → O(N)
- push 반복 → O(N log N)

min(n, abs(sum(works)))
- 이 코드의 핵심 부분이라고 생각된다.
- sum(works)는 전체 작업량이다. 만약 n >= sum(works)라면 모든 작업을 끝낼 수 있기 때문에 반복 횟수를 줄였다.
'''
from heapq import heapify, heappush, heappop
def solution(n, works):
    heapify(works := [-i for i in works])  # := 변수 할당과 동시에 사용.
    for i in range(min(n, abs(sum(works)))):
        heappush(works, heappop(works)+1)
    return sum([i*i for i in works])

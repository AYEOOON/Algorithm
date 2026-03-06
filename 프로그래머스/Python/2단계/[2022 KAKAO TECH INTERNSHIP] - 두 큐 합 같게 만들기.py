'''
https://school.programmers.co.kr/learn/courses/30/lessons/118667#qna
: 길이가 같은 두 개의 큐가 주어지면, 두 큐의 원소 합을 같게 만들어야 하는 문제

처음에는 실제 큐를 이동시키는 방식으로 문제를 해결하려고 함
하지만 입력 크기가 최대 300,000이기 때문에 단순 시뮬레이션 방식으로는 문제를 풀 수 없음

-> queue1의 합을 특정 값으로 만들자!

[핵심 아이디어]
1. 전체 합 계산 (전체 합을 계산 한 후 목표 값 설정
2. queue1의 합을 target으로 맞추기 (q1 -> q2 or q2 -> q1)
3. 투 포인터 방식으로 해결
    - 만약에 queue1의 합이 targer보다 크다면 : q1에서 원소를 꺼내 q2로 이동
    - 작다면: q2에서 원소를 꺼내 q2로 이동
4. 무한 루프 방지를 위해서 이동 횟수 제한
    - 두 큐를 하나의 배열로 보고 투포인터 관점으로 본다면
    - left 포인터는 최대 2n, right 포인터는 최대 n만큼 이동할 수 있다.
    - 따라서 최대 이동 횟수는 3n이 되며, 이를 초과할 경우 새로운 상태가 나오지 않게 된다.
'''

from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    total = sum1+sum2
    
    if total%2 != 0:
        return -1
    
    target = total//2
    
    count = 0
    limit = len(queue1)*3
    
    while count <= limit:
        
        if sum1 == target:
            return count
        
        if sum1 > target:
            x = q1.popleft()
            q2.append(x)
            sum1 -= x
        
        else:
            x = q2.popleft()
            q1.append(x)
            sum1 += x
            
        count += 1
        
    return -1

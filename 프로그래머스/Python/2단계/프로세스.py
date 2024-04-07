"""
이 문제에서는 운영체제가 다음 규칙에 따라 프로세스를 관리할 경우 특정 프로세스가 몇 번째로 실행되는지 알아내면 됩니다.

1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
  3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.

현재 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와, 몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때, 
해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.
"""
"""
작업 별로 우선순위를 저장한 딕셔너리를 만들고
제일 높은 우선순위를 저장한 후, 각 상황에 맞게 if문을 짬
"""


# 내 풀이
def solution(priorities, location):
    ready_queue = [i for i in range(len(priorities))]  # 실행 대기 중인 작업들
    run = [] # 실행된 작업
    process = {i: priorities[i] for i in range(len(priorities))} # 작업: 우선순위
    
    while(ready_queue): # 대기 큐에서 하나씩 뽑는 형태라서 조건을 저 형태로 검
        j = ready_queue[0]  # 현재 작업
        m = max(process.values()) # 제일 높은 우선순위
        if process[j] < m:  # 우선순위 낮을 때
            ready_queue.append(ready_queue.pop(0))  # 현재 작업을 다시 뒤로 미룸
        elif process[j] == m:  # 현재 작업 우선 순위가 m과 같을 때 = 제일 높을 때
            run.append(ready_queue.pop(0))  # 실행된 작업 큐에 넣음
            process.pop(j) # 작업 뺴기
            
    return run.index(location)+1


# 다른사람 풀이
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]  # 작업과 우선순위를 동시에 저장함으로써 딕셔너리를 만들지 않음
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):  # 하나라도 True인게 있으면 True (all(): 모두 True여야 True반환)
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

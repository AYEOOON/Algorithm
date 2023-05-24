# 지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

# 지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

# 1. 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 2. 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
# 3. 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다. 

# 첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. 
# 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 
# 연산을 어떻게 구현해야하는지까지 생각하였지만, 큐의 첫번째 원소와 뽑을 숫자가 같지않을 때 처리를 구현하기 어려워 풀이설명을 참고하였다.  


from collections import deque
import sys

N, M = map(int,sys.stdin.readline().split())

queue = deque([i for i in range(1,N+1)])
num = list(map(int,input().split()))
cnt = 0

for i in num:
  while(True):
    if i == queue[0]:  # queue의 맨앞 원소와 i가 같을 경우
      queue.popleft()  # 연산1 수행
      break
    else:   # queue의 맨앞 원소와 i와 같지 않을 경우 queue에서 i가 있는 위치 구하기
      if queue.index(i) < len(queue)/2:  # i가 queue의 앞쪽에 있을 경우
        while(queue[0] != i):  # queue의 맨앞 원소와 i가 다를 때 반복
          queue.append(queue[0])  # 연산2 수행
          queue.popleft()
          cnt += 1

      else:    # i가 queue의 뒷쪽에 있을 경우
        while(queue[0] != i):   
          queue.appendleft(queue[-1])   # 연산3 수행
          queue.pop()
          cnt += 1

print(cnt)

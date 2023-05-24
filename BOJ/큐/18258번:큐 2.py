# 큐의 기능을 구현하는 문제
# 강의에 나온 연습문제와 같은 풀이를 제출하니까 시간초과가 발생!
# 기존의 코드는 list를 사용하여 구현하였는데 이것이 시간초과의 원인이었다. 
# list로 선언해서 pop(0)을 하게되면 첫 번째 요소를 pop하고 나서 나머지 요소들의 인덱스를 1칸씩 당기는 과정에서 O(n)의 계산량이 발생한다. 
# 따라서 list를 deque로 바꾸어 풀었다. 

from collections import deque
import sys
n = int(sys.stdin.readline())

queue = deque()

for i in range(n):
  command = sys.stdin.readline().split()

  if command[0] == 'push':
    queue.append(command[1])

  elif command[0] == 'pop':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])
      queue.popleft()
        
  elif command[0] == 'size':
    print(len(queue))

  elif command[0] == 'empty':
    if len(queue) == 0:
      print(1)
    else:
      print(0)

  elif command[0] == 'front':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])

  elif command[0] == 'back':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[-1])

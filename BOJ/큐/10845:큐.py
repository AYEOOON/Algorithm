# 리스트로 구현한 큐
# 런타임에러 발생
# n+1 => n으로 바꾸니 해결..!

import sys
n = int(sys.stdin.readline())

queue = []

for i in range(n):
  command = sys.stdin.readline().split()

  if command[0] == 'push':
    queue.append(command[1])

  elif command[0] == 'pop':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])
      queue.remove(queue[0])
      

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

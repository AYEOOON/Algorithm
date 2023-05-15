# 스택의 push, pop, size, empty, top의 기능을 구현하는 문제
# 파이썬은 스택구조를 제공하지 않기 때문에 리스트로 표현한다.


import sys
n = int(sys.stdin.readline())   # input()을 사용하면 시간초과 에러가 뜨므로 sys.stdin.readline()을 사용한다.

stack = []
for i in range(n):
  command = sys.stdin.readline().split()

  if command[0] == 'push':
    stack.append(command[1])

  elif command[0] == 'pop':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack.pop())

  elif command[0] == 'size':
    print(len(stack))

  elif command[0] == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)

  elif command[0] == 'top':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])

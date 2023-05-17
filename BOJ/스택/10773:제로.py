# 첫번째 줄에 정수K가 주어진다. 이후 K개의 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
# 스택 기본문제

# 코드 
import sys
k = int(sys.stdin.readline())

stack = []
for i in range(k):
  num = int(input())
  stack.append(num)
  if num == 0:
    stack.pop()
    stack.pop()

print(sum(stack))

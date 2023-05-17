# 첫번째 줄에 정수K가 주어진다. 이후 K개의 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
# 스택 기본문제
# 시간복잡도 : O(N)

# 코드 
import sys
k = int(sys.stdin.readline())

stack = []
for i in range(k):
  num = int(input())
  stack.append(num)
  if num == 0:  # 만약 스택에 입력되는 수가 0이면
    stack.pop()  # 0 pop
    stack.pop()  # 앞에 입력된 수 pop

print(sum(stack))

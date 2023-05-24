# N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어있다.
# 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
# N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
# 1장이 남을 때까지 반복한다. 
# N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하는 문제
# 리스트는 젤 앞의 값을 뺄 수 없어서 deque을 사용하였다.


from collections import deque
import sys
N = int(sys.stdin.readline())

card = deque()

for i in range(N):
  card.append(i+1)
  
while(len(card) != 1):
  card.popleft()
  card.append(card[0])
  card.popleft()

for i in card:
  print(i)

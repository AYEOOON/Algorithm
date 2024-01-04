# 여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다. 
# 여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 
# 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.

# 1. 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

# 예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.
# 여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 
# 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.

# 우선순위가 높은것이 먼저 탈출하는건 구현이 쉬웠지만, 정해진 숫자의 순서를 구현하는 것에서 애먹었다. 

# 내 풀이
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
  # 문서의 개수 N,  몇 번째로 인쇄되었는지 궁금한 문서가 
  # 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M
  N, M = map(int,input().split())
  
  nums = deque(map(int,input().split())) # N개 문서의 중요도
  idx = deque(i for i in range(N))  # 입력받은 우선순위의 인덱스를 저장하는 배열
  cnt = 0  # 몇 번째로 인쇄할지 카운트하는 변수
  while nums:
    if nums[0] == max(nums):  # # 현재 문서가 중요도가 제일 높다면
      cnt += 1  # 몇 번째로 출력 되는지 카운트

      if idx[0] == M:  # 궁금한 문서인지 확인
        print(cnt)
        break

      else:  # 궁금한 문서가 아니라면 리스트에서 탈출
        nums.popleft()
        idx.popleft()

    else:  # 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면
      nums.append(nums[0])  # 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치
      nums.popleft()
      idx.append(idx[0])
      idx.popleft()

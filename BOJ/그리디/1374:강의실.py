"""
N개의 강의가 있다. 우리는 모든 강의의 시작하는 시간과 끝나는 시간을 알고 있다. 
이때, 우리는 최대한 적은 수의 강의실을 사용하여 모든 강의가 이루어지게 하고 싶다.
물론, 한 강의실에서는 동시에 2개 이상의 강의를 진행할 수 없고, 한 강의의 종료시간과 다른 강의의 시작시간이 겹치는 것은 상관없다. 
필요한 최소 강의실의 수를 출력하는 프로그램을 작성하시오.
"""

# 강의 시작 시간을 기준으로 오름차순 정렬한 뒤, 이를 하나씩 탐색한다.
# 강의 끝나는 시간을 기준으로 최소힙을 구성해 시작 시간보다 일찍 끝나는 강의는 모두 뺀다.
# 매번 강의를 탐색할 때마다 최소힙의 개수를 구해 이의 최대값을 구한 뒤, 이를 출력한다. (이 부분이 생각해내기 어려웠다.)

# 내 풀이
import sys
import heapq
input = sys.stdin.readline

N = int(input())

lacture = []
room = []

for _ in range(N):
  num, start, end = map(int,input().split())
  lacture.append([num, start, end])

lacture = sorted(lacture, key = lambda x: x[0])
lacture = sorted(lacture, key = lambda x: x[1])

cnt = 0

for n,s,e in lacture:
  while(room and room[0] <= s):
    heapq.heappop(room)
  heapq.heappush(room,e)
  cnt = max(cnt, len(room))

print(cnt)

# 달팽이는 높이가 V미터인 나무 막대를 올라간다. 낮엔 A미터 올라갈 수 있으며, 밤엔 B미터 미끄러진다.
# 정상에 올라간 후에 미끄러지지 않는 것을 유의하며, 나무막대를 모두 올라가려면 며칠이 걸리는지 구하는 문제
# 시간제한이 있는 문제여서 반복문을 쓰지 않는 것이 중요하다. 


# 내 풀이

import sys
import math                 # math 모듈

input = sys.stdin.readline

A, B, V = map(int,input().split())

day = (V - B) / (A - B)      # day = V / (A - B)로 써버리면 정상에 올라가도 미끄러져, 다시 올라가야함
print(math.ceil(day))        # ceil()는 괄호 안에 있는 것을 올림해줌. 올림처리를 하여 4.2일도 5일로 만듦



# 시간초과된 코드

A, B, V = map(int,input().split())
day = 0
height = 0

while True:
  day += 1
  height += a
  if height == v:
    print(day)
    break
  height -= b

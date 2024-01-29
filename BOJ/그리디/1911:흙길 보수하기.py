"""
어젯밤 겨울 캠프 장소에서 월드 본원까지 이어지는, 흙으로 된 비밀길 위에 폭우가 내려서 N(1 ≤ N ≤ 10,000)개의 물웅덩이가 생겼다. 
월드학원은 물웅덩이를 덮을 수 있는 길이가 L(1 ≤ L ≤ 1,000,000)인 널빤지들을 충분히 가지고 있어서, 이들로 다리를 만들어 물웅덩이들을 모두 덮으려고 한다.
물웅덩이들의 위치와 크기에 대한 정보가 주어질 때, 모든 물웅덩이들을 덮기 위해 필요한 널빤지들의 최소 개수를 구하여라.
"""
"""
1. 주어진 웅덩이의 좌표는 겹치지 않으므로 웅덩이의 시작 위치가 작은 순으로 오름차순 정렬한다.
2. 웅덩이를 하나씩 탐색하며 그 웅덩이를 커버할 수 있는 널판지의 개수를 센다.
3. 이때 이전 웅덩이에서 널판지를 걸쳤을 때 현재 탐색 중인 웅덩이까지 조금이라도 커버한다면 그 길이를 계산해주고 널판지를 추가한다. 만약 길이가 닿지 않는다면 해당 널판지의 위치를 현재 웅덩이의 시작 위치로 초기화한다.
4. 모든 웅덩이를 탐색한 뒤 총 사용한 널판지의 개수를 출력한다.
"""

# 내 풀이
import sys
input = sys.stdin.readline

N, L = map(int,input().split())

pool = []
nullpan_G = 0

for i in range(N):
  a,b = map(int,input().split())
  pool.append([a,b])

pool = sorted(pool, key = lambda x : x[0])
point = pool[0][0] # 널빤지를 이어붙인 끝자락

for s, e in pool:
  if point > e:
    continue
  elif point < s:
    point = s
  diff = e - point
  cnt = 1
  if diff%L == 0:
    cnt = 0
  count = diff//L + cnt
  point += count * L  # 시작점에서 널빤지를 이어붙인 마지막 끝자락
  nullpan_G += count 

print(nullpan_G)

"""
그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.
최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.
"""
"""
<크루스칼 알고리즘>
1. 주어진 정점과 간선을 간선 기준으로 오름차순 정렬한다.
2. 가중가치 가장 낮은 간선부터 순회하면서
3. 이 간선이 추가된다면 사이클이 발생되는지 확인한다. 
    - 사이클이 발생된다면, coutinue
    - 사이클이 발생되지 않는다면 추가한다.

<사이클 발생 여부 확인>
Union-find를 이용한다. 
요소의 부모를 찾는 함수와 부모를 확인한 후 작은 쪽을 부모로 설정하는 함수를 확인한다. 
두개의 요소가 입력이 같다면 같은 집합에 있는 것이고, 없다면 집합에 존재하지 않는 다는 것을 의미한다.
"""

# 내 풀이
import sys
input = sys.stdin.readline

def find(x):
  if link[x] == x:
    return x
  link[x] = find(link[x])
  return link[x]
  
def union(a,b):
  a = find(a)
  b = find(b)

  if a < b :
    link[b] = a
  else:
    link[a] = b

V, E = map(int,input().split())
line = []

link = [x for x in range(V+1)]
d, c = 0,0

for i in range(E):
  A, B, C = map(int,input().split())
  line.append([A,B,C])

line.sort(key = lambda x: x[2])

for a,b,v in line:
  if find(a) != find(b):
    union(a,b)  # Union함수를 사용하지 않고 그냥 b의 부모에 a를 할당하였더니 시간초과가 발생했다.
    d += v

print(d)


# 다른사람 풀이(프림)
"""
<프림 알고리즘>
임의의 정점 하나를 선택해서 시작
선택한 정점과 인접하는 정점들 중 가중치가 최소인 정점을 선택
모든 정점이 선택될 때까지 반복
"""
from heapq import heappush, heappop
import sys; input=sys.stdin.readline

def prim(start, weight):
    visit = [0] * (V + 1) # 정점 방문 처리
    q = [[weight, start]] # 힙 구조를 사용하기 위해 가중치를 앞에 둠
    ans = 0 # 가중치 합
    cnt = 0 # 간선의 개수
    while cnt < V: # 간선의 개수 최대는 V-1
        k, v = heappop(q)
        if visit[v]: continue # 이미 방문한 정점이면 지나감
        visit[v] = 1 # 방문안했으면 방문처리
        ans += k # 해당 정점까지의 가중치를 더해줌
        cnt += 1 # 간선의 갯수 더해줌
        for u, w in G[v]: # 해당 정점의 간선정보를 불러옴
            heappush(q, [w, u]) # 힙에 넣어줌
    return ans

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])

print(prim(1, 0))

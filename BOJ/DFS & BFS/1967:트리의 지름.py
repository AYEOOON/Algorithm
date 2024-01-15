"""
트리(tree)는 사이클이 없는 무방향 그래프이다. 
트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 
트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 
이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.
이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 
정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.
입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오.
"""
"""
dfs는 시작 노드에서 모든 노드들을 끝까지 탐색하면서 시작 노드와 얼마나 거리가 떨어졌는지만 알 수 있다
1번 노드를 시작으로 dfs를 돌려서 전부다 탐색하고 나면 1번 노드와 가장 먼 거리에 있는 노드를 찾아서 그것을 시작 노드로 다시 dfs를 돌리는 것이다.
어떤 임의의 노드를 시작점으로 그 노드와 가장 먼 지점의 노드를 찾아내서 그 노드를 다시 시작점으로 가장 먼 지점의 노드를 찾아내면 최대 지름이 된다는 얘기이다.
여기서 가장 큰 값을 뽑아내면 그것이 최대 지름이 된다.
"""

# 풀이
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(1,N):
  a,b,c = map(int, input().split())  # a-부모노드 , b-자식노드, c-가중치
  graph[a].append([b,c])
  graph[b].append([a,c])

distance = [-1] * (N+1)
distance[1] = 0

def dfs(v, d):
  for i in range(len(graph[v])):
    next, nextdis = graph[v][i]
    if distance[next] == -1:
      distance[next] = nextdis + d
      dfs(next, distance[next])

dfs(1,0)
max_idx = distance.index(max(distance)) # 1번에서 가장 먼 노드의 인덱스

distance = [-1] * (N+1)  # 거리 초기화
distance[max_idx] = 0  # 가장 먼 인덱스부터 다시 시작 
dfs(max_idx, 0) 

print(max(distance))

"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
정점 번호는 1번부터 N번까지이다.

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
"""

# 내 풀이(재귀)
import sys
input = sys.stdin.readline

N, M, V = map(int,input().split())

# 행렬 만들기
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
  a,b = map(int,input().split())
  graph[a][b] = graph[b][a] = 1

# 방문여부 체크 리스트
visited1 = [False] * (N+1)
visited2 = [False] * (N+1)

# dfs 함수
def DFS(v):
  visited1[v] = True  # 방문처리
  print(v, end = " ")
  for i in range(1, N+1):
    if visited1[i] == False and graph[v][i] == 1:
      DFS(i)

# bfs 함수
def BFS(v):
  visited2[v] = True # 방문처리
  queue = [v]
  while(queue):
    v = queue.pop(0) # 방문노드 제거
    print(v, end = ' ')
    
    for i in range(1, N+1):
      if visited2[i] == False and graph[v][i] == 1:
        queue.append(i)
        visited2[i] = True # 방문처리
      

DFS(V)
print()
BFS(V)

"""
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
컴퓨터와 네트워크상에서 연결되어 있지 않으면 영향을 받지 않는다.
어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
"""

# 내 풀이
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

computers = [[0 for _ in range(N+1)] for i in range(N+1)]  # 연결된 컴퓨터를 나타내는 그래프 생성

for _ in range(M):
  a,b = map(int,input().split())
  computers[a][b] = computers[b][a] = 1  # 서로 연결된 컴퓨터들

visited = [False] * (N+1)

cnt = 0

def dfs(v):  # 너비 우선 탐색을 이용한 풀이
  global cnt
  visited[v] = True
  for i in range(1, N+1):
    if visited[i] == False and computers[v][i] == 1:
      cnt += 1
      dfs(i)


def bfs(v):  # 깊이 우선 탐색을 이용한 풀이
  global cnt
  queue = [v]
  visited[v] = True

  while queue:
    v = queue.pop(0)
    for i in range(1,N+1):
      if visited[i] == False and computers[v][i] == 1:
        queue.append(i)
        visited[i] = True
        cnt += 1
        

bfs(1)
print(cnt)

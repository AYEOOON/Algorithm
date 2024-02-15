"""
어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다. 
한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다.
배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다. 
0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.
"""
"""
2667: 단지번호 붙이기와 비슷한 문제
방문 여부를 나타내는 배열을 사용하는 대신, 1을 0으로 바꿔줌으로써 방문 표시
탐색을 할 때마다 dfs함수 호출, 벌래 수 1 증가
"""

# 내 풀이(DFS 사용)
import sys
sys.setrecursionlimit(10000) # 재귀 깊이 설정
input = sys.stdin.readline

T = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x,y):
  grd[x][y] = 0  # 방문표시
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < M and grd[nx][ny] == 1:
      grd[nx][ny] = 0
      dfs(nx, ny)
  
for _ in range(T):
  M, N, K = map(int, input().split())
  grd = [[0 for _ in range(M+1)] for _ in range(N+1)]
  for _ in range(K):
    X, Y = map(int,input().split())
    grd[Y][X] = 1  # 입력이 가로, 세로가 바뀌어 입력되어 주의해야함

  cnt = 0
  for i in range(N+1):
    for j in range(M+1):
      if grd[i][j] == 1:  # 만약 배추가 있으면
        dfs(i, j)  # 탐색
        cnt += 1
  print(cnt)



# 다른사람 풀이(BFS)
from collections import deque
t = int(input()) # 몇 번의 테스트케이스인지

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(graph, x, y): # bfs 함수 구현
    q = deque()
    q.append([x, y])
    graph[x][y] = 0 # 방문 처리; 처리 방식: 표기된 1을 0으로 바꾸기
    
    while q: # q가 비었다 = 탐색 가능한 연속 영역 모두 탐색하였다.
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 1: # 배추밭 범위를 벗어나지 않고 미방문한 좌표인 경우
                q.append([nx, ny])
                graph[nx][ny] = 0


for _ in range(t):  
    m, n, k = map(int, input().split())
    graph = [[0]*(n) for _ in range(m)] # 빈 배추밭
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1 # 배추 위치 표기
        
    cnt = 0
    for j in range(m):
        for k in range(n):
            if graph[j][k] == 1:
                bfs(graph, j, k)
                cnt+=1 # bfs 함수 들어갈때마다 count; 하나의 연속 영역이 끝날 때마다
    print(cnt)

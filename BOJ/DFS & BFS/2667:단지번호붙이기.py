""" 
아래와 같이 정사각형 모양의 지도가 있다. 

    0110100
    0110101
    1110101
    0000111
    0100000
    0111110
    0111000

1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
대각선상에 집이 있는 경우는 연결된 것이 아니다.  

지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
"""

# 내 풀이(DFS)
import sys
input = sys.stdin.readline

N = int(input())

home = []

for i in range(N):
  home.append(list(map(int,input().rstrip())))

cnt = 0
town = []

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

def dfs(x,y):
  global cnt 
  # 탐색한 부분은 1을 0으로 바꿔준다. 
  home[x][y] = 0  # 이 부분을 if문 아래에 뒀을 때 출력은 같았지만 결과는 틀렸었다. 이유는..아직 모른다. 
  cnt += 1 # 집의 수
  for i in range(len(dx)):  # 위, 아래, 좌, 우 탐색
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < N and home[nx][ny] == 1:
      dfs(nx, ny)
  return cnt


for i in range(N):
  for j in range(N):
    if home[i][j] == 1:  # 어디서부터 탐색하는지 정해지지 않아 첨부터 탐색하여 1이 있으면 탐색시작
      town.append(dfs(i, j))
      cnt = 0

print(len(town))
for k in sorted(town):  # 오름차순 출력
  print(k)



# 다른 풀이(BFS)
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, a, b):
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])

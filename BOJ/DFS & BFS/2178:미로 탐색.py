""" 
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
BFS를 사용하는 문제
"""

"""
1. graph[0][0]부터 (실제 위치는 (1, 1)) bfs를 이용해 동, 서, 남, 북을 검사하여 이동했을 때 1인 값을 찾는다. 
-> 값이 1 이어야 이동할 수 있기 때문에
2. 만약 1이라면 그 전 값에 +1을 하여 이동할 때 지나야 하는 최소 칸 수를 더해준다.
3. 이렇게 쭉 검사 하다보면 마지막 graph[n-1][m-1]에는 최소 칸 수의 최종값이 들어가게 된다.

풀이 참고 : https://blog.encrypted.gg/941
"""

# 내 풀이
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

graph = []
for _ in range(N):
  # readline의 경우 맨 뒤에 '\n'까지 입력받으므로 제거해줘야 함
  line = list(map(int,input().rstrip()))   # split()을 사용하면 [011..]이렇게 입력받아서 틀렸는데, rstrip()을 사용하여 해결하였다. 
  graph.append(line)

def BFS(a,b):
  queue = [(a,b)]

  while(queue):
    a,b = queue.pop(0)
    
    for i in range(len(dx)):
      nx = a+dx[i]
      ny = b+dy[i]
      
      if (0 <= nx < N) and (0 <= ny < M) and graph[nx][ny] == 1:
        queue.append((nx,ny))
        graph[nx][ny] = graph[a][b] + 1

  return graph[N-1][M-1]
      
print(BFS(0,0))

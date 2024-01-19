"""
역사, 그 중에서도 한국사에 해박한 세준이는 많은 역사적 사건들의 전후 관계를 잘 알고 있다. 
즉, 임진왜란이 병자호란보다 먼저 일어났으며, 무오사화가 기묘사화보다 먼저 일어났다는 등의 지식을 알고 있는 것이다.

세준이가 알고 있는 일부 사건들의 전후 관계들이 주어질 때, 주어진 사건들의 전후 관계도 알 수 있을까? 이를 해결하는 프로그램을 작성해 보도록 하자.
"""
"""
처음에는 사건들을 모두 배열에 넣은 뒤, 정렬하고 중복사건을 없애서 인덱스로 풀려고 했으나, 풀지 못했다. 
그래서 알고리즘에 플로이드 워셜로 분류되어있어서 플로이드워셜을 이용하여 풀게되었다. 
플로이드 워셜은 시작점에서 중간점을 거쳐서 도착점까지 갈 수 있는지 없는지 혹은, 갈 수있다면 최단 경로는 무엇인지 3중 for문으로 구할 수 있는 알고리즘이다.
이 문제도 시작점과 중간점을 비교했을 때, 시작점이 먼저이고, 중간점과 도착점을 비교했을 때 중간점이 먼저이기 때문에 시작점이 도착점을 비교하면 시작점이 먼저라고 결론을 낼 수 있다.

사건들을 0으로 채워진 배열에 1로 저장하고, 플로이드워셜을 이용해 시작점에서 중간점을 거쳐서 도착하는 경로가 있으면 1로 저장한다.
*BFS로 풀면 시간초과가 발생한다. 
"""

# 내 풀이
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

floyd = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(k):
  a, b = map(int,input().split())
  floyd[a][b] = 1

for i in range(1,n+1):  # 시작
  for j in range(1, n+1):  # 중간
    for k in range(1, n+1):  # 끝
      if floyd[j][i] + floyd[i][k] == 2:  # 중간을 거쳐서 가는 경로가 있으면
        floyd[j][k] = 1 

s = int(input())
want = []
for _ in range(s):
  c,d = map(int,input().split())
  if floyd[c][d] == 1:  # 앞에 있는 사건이 먼저 일어났다면
    print(-1)
  elif floyd[d][c] == 1:  # 뒤에 있는 사건이 먼저 있어났다면
    print(1)
  else:
    print(0)



# 다른사람 풀이
import sys
input = sys.stdin.readline
INF = float('inf')
n, k = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    i, j = map(int, input().split())
    graph[i][j] = -1
    graph[j][i] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][k] == graph[k][b] != INF:
                graph[a][b] = graph[a][k]

s = int(input())

for _ in range(s):
    a, b = map(int, input().split())
    if graph[a][b] == INF:
        print(0)
    else:
        print(graph[a][b])

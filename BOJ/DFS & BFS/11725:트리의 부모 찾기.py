""" 
루트 없는 트리가 주어진다. 
이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
"""
""" 
처음엔 bfs의 탐색 순서를 저장하여 인덱스에서 2를 나누어 부모 노드를 찾으려고 했지만, 하나가 맞지 않아서 실패했다. 
그래서 다른사람의 풀이를 참고하여 딕셔너리로 연결된 트리를 저장한 다음 bfs를 사용하여 부모노드를 찾는 방법을 이용했다. 

탐색 순서대로 큐에 넣고, 배열하나를 더 만들어서 부모 노드를 저장해주는 방식이다. 
"""

# 내 풀이
import sys
input = sys.stdin.readline

N = int(input())

tree = dict()

# 딕셔너리에 노드 추가
for i in range(1, N+1):
  tree[i] = []

# 연결된 노드를 저장하는 부분
for _ in range(N-1):
  a, b = map(int,input().split())
  tree[a].append(b)
  tree[b].append(a)

parent = [0] * (N+1) # 부모 노드를 저장하는 배열

def bfs(v, tree):
  queue = [v]
  while queue:
    v = queue.pop(0)
    for i in tree[v]:
      if parent[i] == 0 and i != 1:  # 부모노드가 갱신이 되지 않고, 루트노드가 아니면
        parent[i] = v  # 부모노드 저장
        queue.append(i)

bfs(1, tree)
for i in range(2, N+1): # 0, 1을 제외한 나머지 출력
  print(parent[i])


# 다른사람 풀이(dfs)
import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]  # 리스트로 트리 저장
parent = [0] * (N + 1)

for _ in range(N - 1):  # 간선의 갯수 = 노드 개수 - 1
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(v):
    for i in tree[v]:
        if parent[i] == 0:
            parent[i] = v
            dfs(i)
dfs(1)

for j in range(2, len(parent)):
    print(parent[j])

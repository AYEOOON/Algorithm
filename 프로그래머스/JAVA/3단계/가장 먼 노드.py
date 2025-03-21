"""
BFS 사용

1️⃣ 그래프를 인접 리스트로 표현
  - defaultdict(list)를 사용하여 graph[node] = [연결된 노드들] 형태로 저장
2️⃣ BFS를 사용하여 최단 거리 계산
  - Queue를 사용하여 1번 노드부터 탐색
  - visited 또는 distance 딕셔너리를 사용하여 각 노드까지의 거리 저장
  - 방문한 노드는 다시 방문하지 않도록 처리
3️⃣ 최대 거리 찾고 개수 반환
  - distance 딕셔너리에서 최댓값을 찾고, 그 값과 같은 거리의 노드 개수를 반환

"""

from collections import defaultdict
import queue

def solution(n, edge):
    # 1️⃣ 그래프 생성 (인접 리스트)
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # 2️⃣ BFS 준비
    distance = defaultdict(int)  # 노드별 거리 저장
    Q = queue.Queue()
    Q.put(1)  # 1번 노드부터 탐색 시작
    distance[1] = 0  # 시작 노드 거리 0
    
    # 3️⃣ BFS 탐색
    while not Q.empty():
        node = Q.get()
        
        for neighbor in graph[node]:  # 연결된 노드 탐색
            if neighbor not in distance:  # 방문하지 않은 노드라면
                distance[neighbor] = distance[node] + 1  # 거리 갱신
                Q.put(neighbor)

    # 4️⃣ 최장 거리 노드 개수 찾기
    max_distance = max(distance.values())
    return list(distance.values()).count(max_distance)

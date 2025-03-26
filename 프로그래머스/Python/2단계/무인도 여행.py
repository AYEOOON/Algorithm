"""
🚀 풀이 방법 (BFS 탐색)

1. 문자열을 2D 리스트로 변환 (maps_list)
→ 문자열은 불변(immutable)이므로, 수정이 가능한 리스트로 변환

2. BFS로 연결된 숫자 그룹의 총합 계산
→ X가 아닌 숫자부터 시작하여, BFS로 탐색하며 숫자를 누적

3. 방문한 지역은 "X"로 변경하여 중복 탐색 방지

4. 계산된 모든 그룹의 합을 오름차순 정렬하여 반환
"""

import queue  # BFS 탐색을 위한 queue 모듈 임포트

def solution(maps):
    answer = []  # 섬에서 머무를 수 있는 날짜를 저장할 리스트
    n = len(maps)  # 지도(map)의 행 개수
    m = len(maps[0])  # 지도(map)의 열 개수
    
    # 상, 하, 좌, 우 이동을 위한 방향 벡터
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    # 문자열을 2차원 리스트로 변환 (수정 가능한 형태로 만들기)
    maps_list = []
    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(maps[i][j])  # 문자열을 리스트 형태로 변환하여 추가
        maps_list.append(tmp)

    # BFS 탐색 함수 정의
    def bfs(x, y):
        Q = queue.Queue()  # BFS 탐색을 위한 큐 생성
        Q.put([x, y])  # 현재 위치를 큐에 삽입
        cnt = int(maps[x][y])  # 시작 지점의 숫자를 정수로 변환하여 저장
        maps_list[x][y] = "X"  # 방문한 위치는 'X'로 변경하여 중복 방문 방지
        
        # BFS 실행
        while not Q.empty():
            x, y = Q.get()  # 큐에서 현재 위치를 꺼냄
            
            for i in range(4):  # 상, 하, 좌, 우 탐색
                nx = x + dx[i]
                ny = y + dy[i]

                # 지도 범위를 벗어나지 않고, 미방문 지역일 경우
                if 0 <= nx < n and 0 <= ny < m and maps_list[nx][ny] != "X":
                    cnt += int(maps_list[nx][ny])  # 숫자를 합산
                    maps_list[nx][ny] = "X"  # 방문 처리
                    Q.put([nx, ny])  # 큐에 새로운 좌표 추가
        return cnt  # 연결된 영역의 총 숫자 합 반환
    
    # 지도 전체를 탐색하며 BFS 실행
    for i in range(n):
        for j in range(m):
            if maps_list[i][j] != "X":  # 숫자가 있는 경우 BFS 수행
                cnt = bfs(i, j)  # 해당 위치에서 BFS 실행
                answer.append(cnt)  # 결과값 저장

    # 결과를 오름차순 정렬하여 반환 (없으면 -1 반환)
    return sorted(answer) if answer else [-1]

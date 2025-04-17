"""
1. 시작 위치는 (0, 0)이며, dirs 문자열을 순회하면서 방향대로 이동
2. 이동 시, 현재 위치에서 다음 위치까지의 경로를 path로 저장
3. 같은 길을 양방향 중복 없이 세기 위해, ((x1, y1), (x2, y2))와 ((x2, y2), (x1, y1)) 두 가지를 모두 visited에 넣음
4. 현재 위치 갱신
5. 최종적으로 visited의 길이를 2로 나누어 중복 제거 후 반환
"""

def solution(dirs):
    # 시작 위치
    x, y = 0, 0
    
    # 방문한 경로를 저장할 집합 (양방향 모두 저장)
    visited = set()
    
    # 각 방향에 따른 좌표 변화량 (문제 조건에 맞게 x: 위아래, y: 좌우로 변경)
    move = {
        'U': (1, 0),   # 위로 이동
        'D': (-1, 0),  # 아래로 이동
        'R': (0, 1),   # 오른쪽으로 이동
        'L': (0, -1)   # 왼쪽으로 이동
    }

    # 방향 문자열을 하나씩 처리
    for d in dirs:
        dx, dy = move[d]
        nx, ny = x + dx, y + dy

        # 이동 후 좌표가 범위 내에 있는 경우에만 처리
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            path = ((x, y), (nx, ny))         # 현재 위치 → 다음 위치
            rev_path = ((nx, ny), (x, y))     # 다음 위치 → 현재 위치 (역방향)

            # 이미 방문한 경로가 아니라면 추가
            if path not in visited and rev_path not in visited:
                visited.add(path)
                visited.add(rev_path)

            # 현재 위치 갱신
            x, y = nx, ny

    # 중복 제거를 위해 2로 나누어 반환
    return len(visited) // 2

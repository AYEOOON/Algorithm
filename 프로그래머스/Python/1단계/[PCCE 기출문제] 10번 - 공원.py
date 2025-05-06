"""
- 공원의 자리 배치인 park[i][j]는
  "-1": 비어 있는 자리
  "A" ~ "Z": 사람이 앉아 있는 자리
- 따라서 돗자리는 오직 "-1"로만 이루어진 정사각형 영역에만 깔 수 있다.

- 풀이
1. 큰 돗자리부터 내림차순으로 확인
2. 각 돗자리 크기 s에 대해:
  - park를 순회하며, s x s 크기의 정사각형이 전부 "-1"인지 확인
  - 있으면 바로 해당 크기 리턴
3. 아무것도 없으면 -1 반환

- 핵심
1. i, j: 돗자리를 깔기 시작할 위치 (좌상단)
2. x, y: 깔려야 할 정사각형 내부의 좌표

=> 이중 루프를 사용해서 매 위치마다 정사각형이 유효한지 검사
"""

def solution(mats, park):
    n, m = len(park), len(park[0])
    mats = sorted(mats, reverse=True)
    
    def can_place (size):
        for i in range(n - size + 1):  # park의 행을 돌면서
            for j in range(m - size + 1):  # park의 열을 돌면서
                # (i, j)를 시작점으로 하는 size x size 정사각형이 유효한지 검사
                valid = True
                for x in range(i, i + size):   # 현재 위치에서 size만큼 세로
                    for y in range(j, j + size): # 현재 위치에서 size만큼 가로
                        if park[x][y] != "-1": # 하나라도 사람이 앉아있으면
                            valid = False      # 유효하지 않음
                            break              # 더 이상 확인 안 해도 됨
                    if not valid:
                        break
                if valid:                      # 해당 위치에 깔 수 있다면
                    return True                # True 반환 (깔 수 있음)
                  
    for mat in mats:
        if can_place(mat):
            return mat
    
    return -1

"""
1. 행렬 생성:
    - 1부터 rows * columns까지 값을 순서대로 채운 rows x columns 크기의 2D 배열 maps를 생성

2. 쿼리 처리:
    - 각 쿼리 (x1, y1, x2, y2)에 대해 해당 범위의 테두리를 시계방향으로 회전
    - x1, y1, x2, y2는 1-based index로 주어지므로 이를 0-based index로 변환

3. 테두리 값 추출:
    - 회전할 테두리 값을 순서대로 배열 arr에 저장(위쪽, 오른쪽, 아래쪽, 왼쪽).

4. 최소값 추출:
    - 회전된 테두리에서 최소값을 구하여 answer에 추가

5. 시계방향 회전:
    - arr에서 마지막 값을 첫 번째로 이동시켜 시계방향 회전시키고, 회전된 값을 원래 maps에 반영

6. 결과 반환:
    - 모든 쿼리가 끝난 후, answer 배열을 반환
"""

def solution(rows, columns, queries):
    answer = []  # 결과를 담을 리스트
    
    # 초기 맵 생성
    maps = []  # 행렬을 담을 리스트
    tmp = []  # 각 행을 담을 임시 리스트
    
    # 1부터 rows * columns까지의 숫자를 채운 rows x columns 크기의 행렬 생성
    for i in range(1, rows * columns + 1):
        tmp.append(i)  # 현재 숫자 `i`를 임시 리스트에 추가
        if len(tmp) == columns:  # 한 행이 다 채워졌으면
            maps.append(tmp)  # 해당 행을 maps에 추가
            tmp = []  # 임시 리스트 초기화

    # 각 쿼리마다 회전을 수행
    for x1, y1, x2, y2 in queries:
        # 1-based index를 0-based index로 변환
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        
        arr = []  # 테두리 값들을 저장할 배열
        
        # 1. 위쪽 테두리 (x1, y1)에서 (x1, y2)까지 값 저장
        for i in range(y1, y2 + 1):
            arr.append(maps[x1][i])
        
        # 2. 오른쪽 테두리 (x1+1, y2)에서 (x2, y2)까지 값 저장
        for i in range(x1 + 1, x2 + 1):
            arr.append(maps[i][y2])
            
        # 3. 아래쪽 테두리 (x2, y2)에서 (x2, y1)까지 값 저장
        for i in range(y2 - 1, y1 - 1, -1):
            arr.append(maps[x2][i])
            
        # 4. 왼쪽 테두리 (x2-1, y1)에서 (x1, y1)까지 값 저장
        for i in range(x2 - 1, x1, -1):
            arr.append(maps[i][y1])
        
        # 테두리 값들 중 최소값을 구하여 answer에 추가
        answer.append(min(arr))
        
        # 테두리 값들을 시계방향으로 한 칸 회전
        arr = arr[-1:] + arr[:-1]  # 마지막 값을 맨 앞으로 보냄
        
        # 회전된 값들을 다시 maps의 테두리 위치에 반영
        idx = 0  # arr 배열의 인덱스
        
        # 1. 위쪽 테두리 (x1, y1)에서 (x1, y2)까지 값을 회전된 값으로 채우기
        for i in range(y1, y2 + 1):
            maps[x1][i] = arr[idx]
            idx += 1
        
        # 2. 오른쪽 테두리 (x1+1, y2)에서 (x2, y2)까지 값을 회전된 값으로 채우기
        for i in range(x1 + 1, x2 + 1):
            maps[i][y2] = arr[idx]
            idx += 1
            
        # 3. 아래쪽 테두리 (x2, y2)에서 (x2, y1)까지 값을 회전된 값으로 채우기
        for i in range(y2 - 1, y1 - 1, -1):
            maps[x2][i] = arr[idx]
            idx += 1
            
        # 4. 왼쪽 테두리 (x2-1, y1)에서 (x1, y1)까지 값을 회전된 값으로 채우기
        for i in range(x2 - 1, x1, -1):
            maps[i][y1] = arr[idx]
            idx += 1
    
    # 결과 배열 반환
    return answer

"""
코로나 바이러스 감염 예방을 위해 응시자들은 거리를 둬서 대기를 해야하는데 개발 직군 면접인 만큼
아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.

대기실은 5개이며, 각 대기실은 5x5 크기입니다.
거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.

5개의 대기실을 본 죠르디는 각 대기실에서 응시자들이 거리두기를 잘 기키고 있는지 알고 싶어졌습니다. 
자리에 앉아있는 응시자들의 정보와 대기실 구조를 대기실별로 담은 2차원 문자열 배열 places가 매개변수로 주어집니다.
각 대기실별로 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 배열에 담아 return 하도록 solution 함수를 완성해 주세요.
"""
"""
대기실을 탐색하면서 각각의 원소를 기준으로 상하좌우만 검사
- 원소가 P일때 => 상하좌우로 P가 없어야함
- 원소가 O일때 => 상하좌우로 P가 1개 이하여야함
"""

# 내 풀이
def solution(places):
    answer = [1] * 5
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for i in range(5):
        for j in range(5):
            for k in range(5):  
                if places[i][j][k] == 'P':
                    for l in range(4):
                        nx = j + dx[l]
                        ny = k + dy[l]
                        if 0<=nx<5 and 0<=ny<5:
                            if places[i][nx][ny] == 'P':
                                answer[i] = 0
                if places[i][j][k] == 'O':
                    cnt = 0
                    for l in range(4):
                        nx = j + dx[l]
                        ny = k + dy[l]
                        if 0<=nx<5 and 0<=ny<5:
                            if places[i][nx][ny] == 'P':
                                cnt += 1
                        if cnt >= 2:
                            answer[i] = 0
      return answer

    # for i in range(5):
    #     check = [[0 for _ in range(5)] for _ in range(5)]
    #     for j in range(5):
    #         for k in range(5):
    #             if places[i][j][k] == 'P':
    #                 check[j][k] -= 1
    #                 for l in range(4):
    #                     nx = j+dx[l]
    #                     ny = k+dy[l]
    #                     if 0<=nx<5 and 0<=ny<5:
    #                         check[nx][ny] -= 1
    #             if places[i][j][k] == 'X':
    #                 check[j][k] += 10
    #     for x in range(5):
    #         for y in range(5):
    #             if check[x][y] <= -2:
    #                 answer[i] = 0
    #             else:
    #                 answer[i] = 1
  
# 다른사람 풀이
def check_distance(place):
    # 'P' 값의 좌표만 plist에 추가함.
    plist = [(y, x) for y in range(5) for x in range(5) if place[y][x] == 'P']
 
    # 각 좌표끼리 거리를 계산하고, 거리에 따라 거리두기 여부 판단
    for y, x in plist:
        for y2, x2 in plist:
            dist = abs(y-y2) + abs(x-x2) # 맨해튼 거리
            if dist == 0 or dist > 2: # 같은 좌표이거나 거리가 2이상인 경우 continue
                continue
 
            if dist == 1: # 두 사람 사이의 거리가 1인 경우
                return 0
            elif y == y2 and place[y][int((x+x2)/2)] != 'X':  # 열이 같으나 두 사람 사이에 파티션이 없는 경우
                return 0
            elif x == x2 and place[int((y+y2)/2)][x] != 'X':  # 행이 같으나 두 사람 사이에 파티션이 없는 경우
                return 0
            elif y != y2 and x != x2: # 열/행이 다른경우(대각선), 두 사람 사이 파티션이 없는 경우
                if place[y2][x] != 'X' or place[y][x2] != 'X':
                    return 0
    return 1
 
 
def solution(places):
    answer = []
    # 각 place들을 check_distance함수로 조사
    for place in places:
        answer.append(check_distance(place))
    return answer

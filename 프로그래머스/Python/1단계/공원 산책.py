"""
지나다니는 길을 'O', 장애물을 'X'로 나타낸 직사각형 격자 모양의 공원에서 로봇 강아지가 산책을 하려합니다. 산책은 로봇 강아지에 미리 입력된 명령에 따라 진행하며, 명령은 다음과 같은 형식으로 주어집니다.

["방향 거리", "방향 거리" … ]
예를 들어 "E 5"는 로봇 강아지가 현재 위치에서 동쪽으로 5칸 이동했다는 의미입니다. 로봇 강아지는 명령을 수행하기 전에 다음 두 가지를 먼저 확인합니다.

주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
위 두 가지중 어느 하나라도 해당된다면, 로봇 강아지는 해당 명령을 무시하고 다음 명령을 수행합니다.
공원의 가로 길이가 W, 세로 길이가 H라고 할 때, 공원의 좌측 상단의 좌표는 (0, 0), 우측 하단의 좌표는 (H - 1, W - 1) 입니다.

공원을 나타내는 문자열 배열 park, 로봇 강아지가 수행할 명령이 담긴 문자열 배열 routes가 매개변수로 주어질 때, 로봇 강아지가 모든 명령을 수행 후 놓인 위치를 [세로 방향 좌표, 가로 방향 좌표] 순으로 배열에 담아 return 하도록 solution 함수를 완성해주세요.
"""

# 내 풀이
def solution(park, routes):
    start = []
    move = {'E': [0,1], 'W': [0,-1], 'N': [-1,0], 'S': [1,0]}
    arr = []
    
    # 시작점 찾기
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                start.append(i)
                start.append(j)

    # 방향과 거리 정리
    for k in routes:
        k = k.split()
        arr.append(k)

    # m = 방향, s = 거리
    for m,s in arr:
        [r, c] = start  # 기존 위치 저장
        if 0 <= start[0]+(move[m][0]*int(s)) < len(park) and 0 <= start[1]+(move[m][1]*int(s)) < len(park[0]):
            for _ in range(int(s)): # 한칸씩 탐색
                if park[start[0]+(move[m][0])][start[1]+(move[m][1])] != 'X':   # 시작지점 'S'도 중복으로 갈 수 있기 때문에 'X'만 아니면됨
                    start[0]+=(move[m][0])
                    start[1]+=(move[m][1])
                else: # 만약 이동 중 'X'가 나오면
                    start = [r,c]  # 기존에 저장된 위치로 되돌아감
                    break
            else:
                continue
    
    return start


# 다른사람 풀이
def solution(park, routes):
    W = len(park[0])
    park = [['X']*(W+2)] + [[*'X'+i+'X'] for i in park] + [['X']*(W+2)]  # 바운더리를 장애물로 각인 -> 체크하는 로직이 간단해짐

    x,y = 1,0
    while park[x][y]!='S':
        y += 1
        if y>W:
            x,y = x+1,0

    delta = {k:v for k,v in zip('NEWS',[(-1,0),(0,1),(0,-1),(1,0)])}
    for i in routes:
        v,d = i.split()
        for k in range(1,int(d)+1):
            X,Y = x+k*delta[v][0], y+k*delta[v][1]
            if park[X][Y]=='X':
                break
        else:
            x,y = X,Y
    return [x-1,y-1]

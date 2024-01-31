"""
컴퓨터 바탕화면은 각 칸이 정사각형인 격자판입니다. 
파일들은 바탕화면의 격자칸에 위치하고 바탕화면의 격자점들은 바탕화면의 가장 왼쪽 위를 (0, 0)으로 시작해 (세로 좌표, 가로 좌표)로 표현합니다.
빈칸은 ".", 파일이 있는 칸은 "#"의 값을 가집니다.
머쓱이의 컴퓨터 바탕화면의 상태를 나타내는 문자열 배열 wallpaper가 매개변수로 주어질 때 바탕화면의 파일들을 한 번에 삭제하기 위해 최소한의 이동거리를 갖는 드래그의 시작점과 끝점을 담은 정수 배열을 return하는 solution 함수를 작성해 주세요. 
드래그의 시작점이 (lux, luy), 끝점이 (rdx, rdy)라면 정수 배열 [lux, luy, rdx, rdy]를 return하면 됩니다.
"""

# 내 풀이
def solution(wallpaper):
    start_x = 99
    start_y = 99
    end_x = 0
    end_y = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                    start_x = min(start_x, i)
                    start_y = min(start_y, j)
                    end_x = max(end_x, i)
                    end_y = max(end_y, j)    
                
    return start_x, start_y, end_x+1, end_y+1


# 다른사람 풀이
def solution(wall):
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]

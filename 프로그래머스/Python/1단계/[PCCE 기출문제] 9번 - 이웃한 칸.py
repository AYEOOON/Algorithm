""" 
각 칸마다 색이 칠해진 2차원 격자 보드판이 있습니다. 
그중 한 칸을 골랐을 때, 위, 아래, 왼쪽, 오른쪽 칸 중 같은 색깔로 칠해진 칸의 개수를 구하려고 합니다.
보드의 각 칸에 칠해진 색깔 이름이 담긴 이차원 문자열 리스트 board와 고른 칸의 위치를 나타내는 두 정수 h, w가 주어질 때 board[h][w]와 이웃한 칸들 중 같은 색으로 칠해져 있는 칸의 개수를 return 하도록 solution 함수를 완성해 주세요.
"""

# 내 풀이
def solution(board, h, w):
    cnt = 0  # 같은 색으로 색칠된 칸의 개수를 저장할 변수 cnt를 만들고 0을 저장
    color = board[h][w]

    # h와 w의 변화량을 저장할 정수 리스트 dh, dw를 만들고 각각 [0, 1, -1, 0], [1, 0, 0, -1]을 저장
    dh = [1, -1, 0, 0]
    dw = [0, 0, 1, -1]
    
    for i in range(len(dx)):   # 위, 아래, 좌, 우 4번 살펴야하기 때문에 보드의 수가 아닌 변화량 수만큼 반복(여기서 계속 오류가 났었다..)
        # 체크할 칸의 h, w 좌표를 나타내는 변수 h_check, w_check를 만들고 각각 h + dh[i], w + dw[i]를 저장
        h_check = h+dh[i]
        w_check = w+dw[i]
        if (0<=h_check<len(board)) and (0<=w_check<len(board)):  # h_check가 0 이상 n 미만이고 w_check가 0 이상 n 미만이라면
            if board[h_check][w_check] == color:
                cnt += 1
    return len(board), len(dx)


# 다른사람 풀이
def solution(board, h, w):
    answer = 0

    if 0 < h:
        if board[h][w] == board[h-1][w]: answer += 1
    if 0 < w:
        if board[h][w] == board[h][w-1]: answer += 1
    if h < len(board) - 1:
        if board[h][w] == board[h+1][w]: answer += 1
    if w < len(board[0]) - 1:
        if board[h][w] == board[h][w+1]: answer += 1

    return answer

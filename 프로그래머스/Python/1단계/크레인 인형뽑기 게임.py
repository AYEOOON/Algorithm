# "죠르디"는 게임의 재미를 높이기 위해 화면 구성과 규칙을 다음과 같이 게임 로직에 반영하려고 합니다.
# 게임 화면은 "1 x 1" 크기의 칸들로 이루어진 "N x N" 크기의 정사각 격자이며 위쪽에는 크레인이 있고 오른쪽에는 바구니가 있습니다. (위 그림은 "5 x 5" 크기의 예시입니다). 
# 각 격자 칸에는 다양한 인형이 들어 있으며 인형이 없는 칸은 빈칸입니다.
# 모든 인형은 "1 x 1" 크기의 격자 한 칸을 차지하며 격자의 가장 아래 칸부터 차곡차곡 쌓여 있습니다. 
# 게임 사용자는 크레인을 좌우로 움직여서 멈춘 위치에서 가장 위에 있는 인형을 집어 올릴 수 있습니다. 
# 집어 올린 인형은 바구니에 쌓이게 되는 데, 이때 바구니의 가장 아래 칸부터 인형이 순서대로 쌓이게 됩니다. 
# 만약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라지게 됩니다. 
# 크레인 작동 시 인형이 집어지지 않는 경우는 없으나 만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않습니다.
# 게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때, 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요.


# 내 풀이
def solution(board, moves):
    stack = [0]   # 바구니 역할을 해줄 stack을 준비하고, 0을 넣는다.(인덱스 오류를 피하기위해)
    answer = 0
    for i in moves:  # moves를 차례대로 for문을 돌림
        for j in range(len(board)):  # board의 길이만큼 for문을 돌린다. (해당 라인에서 인형을 뽑기 위해)
            if board[j][i-1] == 0:   # 만약 board[j][move - 1]이 0이라면 인형이 없는 것이기 때문에 넘어간다.
                continue
            else:  # 0이 아니라면
                if board[j][i-1] == stack[-1]:  # Stack(바구니)의 가장 윗 요소와 board[j][move - 1]가 같은지 비교한다.
                    stack.pop()
                    board[j][i-1] = 0   # 같다면 인형이 터지는 것이기 때문에 Stack에 pop을 하고 
                    answer += 2      # answer에 2를 더한다.
                else: 
                    stack.append(board[j][i-1])  # 다르다면 Stack에 board[j][move - 1]를 push한다.
                    board[j][i-1] = 0  # 인형을 뽑았으니 0으로 변경
                break
    return answer


# 다른사람 풀이
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer

# 다시풀어보면 좋을거같은 문제

# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다.
# 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 
# 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 
# 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
# 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 
# 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

# 접근 방법
# 1. 다시 칠해야하는 경우
# 1-1. 하나는 맨 왼쪽 위 칸이 흰색인 경우
# 1-2. 하나는 검은색인 경우
# 2. 변을 공유하는 두개의 사각형을 다른 색으로 칠해져 있어야한다. 
# 3. 문제 조건에 따라, 8*8 크기의 체스판으로 잘라내야한다. 
# 행과 열의 인덱스의 합계가 짝수면 처음 색과 같아야, 홀수면 달라야한다. 

# 풀이
N, M = map(int,input().split()) # N,M 입력

board = []  # 체스판을 저장할 배열
result = [] # 결과를 저장할 배열

for i in range(N):
  board.append(input())  # 체스판 입력

for i in range(N-7): # 8*8로 자르기 위해 -7을 해준다. 
  for j in range(M-7):
    b_index = 0 # 흰색으로 시작
    w_index = 0 # 검정색으로 시작

    for a in range(i,i+8): # 시작지점
      for b in range(j,j+8):  # 시작지점
        if (a+b)%2 == 0:  # 짝수인 경우
          if board[a][b] != 'W': # W가 아니면, 즉 B이면
            w_index += 1 # W로 칠하는 갯수
          else: # W일 때
            b_index += 1 # B로 칠하는 갯수
        else: # 홀수 일때
          if board[a][b] != 'W': # W가 아니면, 즉 B이면
            b_index += 1 # B로 칠하는 갯수
          else: # B이면
            w_index += 1  # W로 칠하는 갯수 

    result.append(w_index)  # W로 시작할 때 경우의 수 
    result.append(b_index)  # B로 시작할 때 경우의 수 

print(min(result))  # 최소 횟수 출력

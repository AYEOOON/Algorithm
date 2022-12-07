# 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l)
# 막대를 놓는 방향(d:가로는 0, 세로는 1)
# 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

# 격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.


h,w = map(int,input().split())
n = int(input())                                      # 막대의 갯수 n을 입력받는다.
grid = [list(0 for i in range(w)) for j in range(h)]

for i in range(n):
  l,d,x,y = map(int,input().split())                  # n만큼 l(막대의 길이), d(방향), x, y 좌표를 입력받는다.
  x -= 1
  y -= 1
  if d == 0:                                         # d가 0(가로)일 경우 if문
    for j in range(l):                               # 막대 l의 길이 만큼 for문 반복
      grid[x][y+j] = 1                               # 판에서 y좌표에 막대 길이만큼 1로 변경하여 막대를 표시
  else:
    for j in range(l):
      grid[x + j][y] = 1                               # 판에서 x좌표에 막대 길이만큼 1로 변경하여 막대를 표시

for crd in grid:
  print(*crd)

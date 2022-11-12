# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 
# 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 
# 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.
# 예를 들어 흰색 도화지 위에 세 장의 검은색 색종이를 그림과 같은 모양으로 붙였다면 검은색 영역의 넓이는 260이 된다.
# 이 문제는 좌측 하단의 좌표를 받아 가로와 세로의 길이가 10인 사각형을 1로 표현한다.
# 결국 겹치는 부분들도 다 1로 표현이 될 것이고, 결국엔 2차원 리스트에서 1의 갯수를 구하면 된다.


# 내 풀이 
import sys
input = sys.stdin.readline

N = int(input())
arr = [[0 for _ in range(101)]for _ in range(101)]

for _ in range(N):
  a,b = map(int,input().split())

  for i in range(a,a+10):
    for j in range(b,b+10):
      arr[i][j] = 1

count = 0
for row in arr:
  count += row.count(1)

print(count)

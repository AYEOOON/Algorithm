# N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다. 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.
# 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
# 이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

# 분할 정복을 이용하여 푸는 문제(쿼드트리와 비슷)
# 조건이 만족하지 않는 경우 9개로 쪼개서 다시 푸는 문제
# 9개로 쪼개는 것은 재귀 함수를 호출하여 풀고, 전달인자로 그 9개의 각각 종이 중 가장 왼쪽 위의 좌표와 크기를 넣음
# 조건이 만족하는 경우 해당 값을 +1

# 두단계로 진행
# 1. 모두 같은 색이 아니기 때문에 종이를 9개로 나눔
# 2. 쪼개진 종이를 하나씩 검색하는데, 그 쪼개진 종이의 색이 모두 같은 색이면, 그 색상을 +1하고, 그렇지 않으면 또 9개로 나눔


# 내 풀이
import sys
input = sys.stdin.readline

N = int(input())  # 한변의 길이

arr = [list(map(int, list(input().split()))) for _ in range(N)]   # 배열 입력

zero, mone, pone = 0,0,0  # 값 초기화
def divide(X, Y, N):
  global zero, mone, pone
  paper = arr[X][Y]  

  for i in range(X, X+N):  # 종이를 순회
    for j in range(Y, Y+N):
      if paper != arr[i][j]: # 만약 숫자가 다르면
        for k in range(3):  
          for l in range(3):
            divide(X+k*N//3, Y+l*N//3, N//3)  # 3으로 나눔
        return 
  if paper == 0:
    zero += 1
  elif paper == -1:
    mone += 1
  else:
    pone += 1

  
divide(0,0,N)
print(mone)
print(zero)
print(pone)


# 나누는 과정을 푼 것
if color != paper[i][j]:    
  next_n = N//3
  divide(x, y, next_n) # x=0, k=0, l=0 일때와 동일
  divide(x+next_n, y, next_n) # x=0, k=1, l=0 일때와 동일
  divide(x+(next_n*2), y, next_n) # x=0, k=2, l=0 일때와 동일
  divide(x, y+next_n, next_n) # x=0, k=0, l=1 일때와 동일
  divide(x, y+(next_n*2), next_n) # x=0, k=0, l=2 일때와 동일
  divide(x+next_n, y+next_n, next_n) # x=0, k=1, l=1 일때와 동일
  divide(x+(next_n*2), y+next_n, next_n) # x=0, k=1, l=2 일때와 동일
  divide(x+next_n, y+(next_n*2), next_n) # x=0, k=2, l=1 일때와 동일
  divide(x+(next_n*2), y+(next_n*2), next_n) # x=0, k=2, l=2 일때와 동일
  return

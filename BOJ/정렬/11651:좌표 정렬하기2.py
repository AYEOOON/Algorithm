# 2차원 평면 위의 점 N개가 주어진다. 
# 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
# 좌표 정렬하기와 풀이 비슷함


# 내 풀이
import sys
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
  x,y = map(int, input().split())
  arr.append([x,y])  # x,y 좌표 저장하기
  
arr.sort(key = lambda y: (y[1],y[0]))   # sort의 key를 이용하여 y부터 정렬(항상기억!!)

for i in range(N):
  print(arr[i][0], arr[i][1])

# 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때, n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자
# 2차원 리스트를 사용하는 문제이다.


# 내 풀이
d = [[0 for j in range(19)] for i in range(19)]

n = int(input())
for i in range(n):
  x,y = map(int,input().split())
  d[x-1][y-1]= 1            

for crd in d:
    print(*crd)

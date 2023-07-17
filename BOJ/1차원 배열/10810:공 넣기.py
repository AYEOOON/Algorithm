# 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 
# 또, 1번부터 N번까지 번호가 적혀있는 공을 매우 많이 가지고 있다. 가장 처음 바구니에는 공이 들어있지 않으며, 바구니에는 공을 1개만 넣을 수 있다.
# 공을 어떻게 넣을지가 주어졌을 때, M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램을 작성하시오.
# 한 번 공을 넣을 때, 공을 넣을 바구니 범위를 정하고, 정한 바구니에 모두 같은 번호가 적혀있는 공을 넣는다. 만약, 바구니에 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 공을 넣는다. 공을 넣을 바구니는 연속되어 있어야 한다.


# 내 풀이
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
num = [0]*(N+1)
for i in range(M):
  a,b,c = map(int,input().split())
  for i in range(a, b+1):
    num[i] = c
for i in range(1,N+1):
  print(num[i],end=' ')


# 다른사람 풀이
n,m = map(int, input().split())
s = [0]*(n+1)
for _ in range(m):
    i,j,k = map(int, input().split())
    for x in range(i,j+1):
        s[x] = k
print(*s[1:])   # 리스트를 언패킹 할 때 사용하는 문자!! 꼭 기억

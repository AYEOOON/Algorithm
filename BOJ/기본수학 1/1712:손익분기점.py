# 최초로 이익이 발생하는 시점의 판매량을 출력하고 손익분기점이 존재하지 않으면 -1을 출력하는 문제이다.
# 총수입 = 고정비용 + 가변비용, 판매량을 N이라고 한다면 C*N = A + B*N으로 나타낼 수 있다. 


# 내 풀이

A, B, C = map(int,input().split())

if B >= C:         # 가변비용이 노트북 가격보다 같거나 클 때
  print(-1)

else:
  print(A//(C-B)+1)

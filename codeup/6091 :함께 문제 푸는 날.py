# 3명이 다시 모두 함께 방문해 문제를 풀어보는 날(동시 가입/등업 후 며칠 후?)을 출력한다.


a,b,c = map(int,input().split())

d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)

"""
현재 N개의 앱, A1, ..., AN이 활성화 되어 있다고 가정하자. 
이들 앱 Ai는 각각 mi 바이트만큼의 메모리를 사용하고 있다. 
또한, 앱 Ai를 비활성화한 후에 다시 실행하고자 할 경우, 추가적으로 들어가는 비용(시간 등)을 수치화 한 것을 ci 라고 하자. 
이러한 상황에서 사용자가 새로운 앱 B를 실행하고자 하여, 추가로 M 바이트의 메모리가 필요하다고 하자. 
즉, 현재 활성화 되어 있는 앱 A1, ..., AN 중에서 몇 개를 비활성화 하여 M 바이트 이상의 메모리를 추가로 확보해야 하는 것이다. 
여러분은 그 중에서 비활성화 했을 경우의 비용 ci의 합을 최소화하여 필요한 메모리 M 바이트를 확보하는 방법을 찾아야 한다.
"""
"""
0-1 배낭 문제와 비슷한 문제
memory[i][j] = i번째 물건을 넣었을 때 j의 비용으로 얻을 수 있는 최대 메모리로 두고 2차원 배열을 채운 뒤
처음으로 M이 되는 j값이 답이 되는 문제이다.
"""

# 내 풀이
import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N개의 앱, 최대 바이트 M

m = list(map(int,input().split())) # 앱의 바이트

c = list(map(int,input().split())) # 비활성화하는 경우의 비용

answer = sum(c)  # 최소를 찾기 위해서는 일단 최대로 값을 저장한다. 

memory = [[0 for _ in range(sum(c)+1)] for _ in range(N)]  # 최대 메모리를 저장하는 배열

for i in range(N):
  for j in range(sum(c)+1):
    if j >= c[i]:  # 현재 앱의 비용(c[i])가 j보다 크지 않으면
      memory[i][j] = max(memory[i-1][j], memory[i-1][j-c[i]]+m[i])  # 현재 앱을 끈 뒤의 바이트와 그렇지 않을 경우의 바이트 중 큰 값 저장
      
    else:  # 현재 앱의 비용(c[i])가 j보다 크면
      memory[i][j] = memory[i-1][j]  # 앱을 비활성화 하지 못하므로 이전 값 저장

    if memory[i][j] >= M:  # 만약 M이상이라면 
      answer = min(answer, j) # 현재 비용 j와 이전 비용을 비교해 더 작은 값 저장

if M!=0:
  print(answer)
else:
  print(0)

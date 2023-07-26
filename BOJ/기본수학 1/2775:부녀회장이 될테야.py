# 이 아파트에 거주를 하려면 a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다.
# 아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 
# 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
# 첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다

# 내 풀이
N = int(input())

for i in range(N):
  k = int(input())
  n = int(input())

  f0 = [j for j in range(1,n+1)]   # 0층의 사람들을 f0리스트에 넣어놓는다. 
  
  for i in range(k): # 호 수 만큼 반복
    f = []
    for j in range(n):  
      f.append(sum(f0[:j+1]))  # 새로운 리스트에 각 호수별로 아래층의 1~n호 까지의 합을 넣는다. 
    f0 = f.copy()  # 기존의 리스트에 복사하여 넣는다.

  print(f0[-1])  # k층 n호에 사는 인원수를 출력한다. 

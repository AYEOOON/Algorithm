# 사람의 덩치를 키와 몸무게, 이 두 개의 값으로 표현하여 그 등수를 매겨보려고 한다. 
# 어떤 사람의 몸무게가 x kg이고 키가 y cm라면 이 사람의 덩치는 (x, y)로 표시된다. 두 사람 A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때 x > p 그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"고 말한다.
# N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다. 만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다. 
#  입력받은 몸무계와 키를 각각의 사람마다 묶어서 리스트에 저장해준 후 자신보다 몸무게 그리고 키가 모두 큰 사람의 수를 세는 것으로 해결할 수 있다. 

# 내 풀이
import sys
input = sys.stdin.readline

N = int(input())
arr = []  # 입력받은 정보를 저장할 리스트 
rank = [] # 등수 정보를 저장할 리스트

for i in range(N):
  w,h = map(int,input().split())
  arr.append([w,h]) # 몸무게와 키를 묶어서 append
  
for i in range(N):
  count = 0
  for j in range(N):
    if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]: # 몸무게와 키 모두 자신보다 큰 사람의 수를 센다
      count += 1
  rank.append(count+1)   # 덩치 등수는 자신보다 몸무계 키 모두 큰 사람의 수 + 1 이므로 count + 1을 ans에 append한다.

print(*rank)


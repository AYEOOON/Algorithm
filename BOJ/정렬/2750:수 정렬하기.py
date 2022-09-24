# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하는 문제
# 시간복잡도가 O(n2)인 정렬 알고리즘으로 풀 수 있다. 

# 내 풀이

N = int(input())           # 첫째 줄에서 이후 주어질 수의 개수를 입력받음
num_list = []              # num_list를 통해 숫자들의 리스트를 만듦

for i in range(N):         # N만큼 반복함
    num_list.append(int(input()))   # 입력받은 숫자들을 num_list에 저장한다.
num_list = sorted(num_list)         # num_list를 sorted로 정렬한다. 
for i in range(len(num_list)):      # 요소들을 하나씩 출력한다.
  print(num_list[i])
  
  

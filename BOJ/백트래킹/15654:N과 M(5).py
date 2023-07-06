# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.
# N개의 자연수 중에서 M개를 고른 수열
# 첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
# 둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.(중요)
# 여러번 실패했는데 그 이유는 만약 12,13,110이 들어오면 110,12,13으로 정렬되기 때문이였다. 
# 따라서 int로 입력받은 후 정렬한 뒤 인덱스로 숫자를 받아야한다!

# 내 풀이
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
arr = []
num.sort()

def func(num):
  if(len(arr) == m):
      print(' '.join(map(str,arr)))
      return 

  for i in range(n):  # 입력받은 숫자의 갯수만큼 반복
    if num[i] not in arr:  # i번째의 숫자가 있지 않으면
      arr.append(num[i])  # 배열에 넣기
      func(num)  # 함수호출
      arr.pop()  # 제일 뒤 숫자 빼기

func(num)

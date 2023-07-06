# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.
# 이 문제 시리즈는 각 코드가 어떤 역할을 수행하는지 잘 파악해야하는 것 같다. 


# 내 풀이
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

def func():
  if(len(arr) == m):
      print(' '.join(map(str,arr)))
      return 

  for i in range(1,n+1):
      arr.append(i)  # 기존에 있던 방문여부를 묻는 조건문 삭제
      func()
      arr.pop()

func()

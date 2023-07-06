# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
# 15649번과 거의 동일하지만 이 문제에서는 [1,2], [2,1]과 같은 경우는 중복되는 경우로 보고 [1,2]만 출력해야한다


# 풀이
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

def func(start):    # start 변수 추가
  if(len(arr) == m):
      print(' '.join(map(str,arr)))
      return 

  # 기존에는 1부터 n까지 모든 숫자를 사용했지만 [2,1]과 같이 앞의숫자가 뒤의숫자보다 작은경우를 제외하기위해 start부터 n까지 숫자를 사용한다.
  for i in range(start,n+1):
    if i not in arr:
      arr.append(i)
      func(i+1)   # 재귀함수를 호출할때는 i를 이용하여 자신의 다음숫자를 부르게된다.
      arr.pop()

func(1)

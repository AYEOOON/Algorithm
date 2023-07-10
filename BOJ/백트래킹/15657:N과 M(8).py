# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
# 중복을 허용하기 위해 if~를 없앤 후, start를 매개변수로 주어 오름차순으로 만듦

# 내 풀이
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
arr = []
num.sort()

def func(start):
  if(len(arr) == m):
      print(' '.join(map(str,arr)))
      return 

  for i in range(start, n):
      arr.append(num[i])
      func(i)
      arr.pop()

func(0)

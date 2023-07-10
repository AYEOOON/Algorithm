# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 중복을 허용하기 위해 방문확인 배열 삭제


# 내 풀이
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = sorted(map(int, input().split()))
arr = []


def func():
  if(len(arr) == m):
      print(' '.join(map(str,arr)))
      return 

  pre = 0
  for i in range(n):
    if (pre != num[i]):
      arr.append(num[i])
      pre = num[i]
      func()
      arr.pop()

func()

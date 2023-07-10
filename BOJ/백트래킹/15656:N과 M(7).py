# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.
# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

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

  for i in range(n):
      arr.append(num[i])   # 중복을 허용하려면 if num[i] not in arr: 이부분을 삭제하면 된다. 
      func(num)
      arr.pop()

func(num)

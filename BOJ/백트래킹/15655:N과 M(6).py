# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.
# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.


# 내 풀이
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
arr = []
num.sort()

def func(start):   # start를 매개변수로 주어 재귀함수가 호출되었을 때, 현재 인덱스에 +1을 매개변수로 줌
  if(len(arr) == m):
      print(' '.join(map(str,arr)))
      return 

  for i in range(start, n):
    if num[i] not in arr:
      arr.append(num[i])
      func(i)
      arr.pop()

func(0)

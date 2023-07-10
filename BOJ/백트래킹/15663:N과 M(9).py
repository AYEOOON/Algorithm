# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# N개의 자연수 중에서 M개를 고른 수열
# set을 사용하려하였지만 실패
# pre 변수로 중복된 수열을 출력하는 것을 방지
# 만약, [9, 7, 9, 1]이라는 배열이 입력으로 들어오면 중복된 수열 1, 9와 1, 9가 출력되는 경우를 방지함
# visited로 숫자의 방문여부를 판단한다.

# 내 풀이
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = sorted(map(int, input().split()))
arr = []
visited = [False] * n   # 방문확인 배열 선언

def func():
  if(len(arr) == m):
      print(' '.join(map(str,arr)))
      return 

  pre = 0   # 어떤 원소를 담아줬는지 확인할 변수
  for i in range(n):
    if (visited[i] == 0) and (pre != num[i]):  # 중복순열을 방지하기 위한 조건문
      arr.append(num[i])  # 배열에 담기
      visited[i] = 1  # 방문처리
      pre = num[i]  # 최근에 담은 원소 pre에 저장
      func()
      visited[i] = 0  # 방문처리 원복
      arr.pop()   # 다른원소를 넣기 위해 pop

func()

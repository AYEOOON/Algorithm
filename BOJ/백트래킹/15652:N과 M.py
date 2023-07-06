# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순(오름차순)이라고 한다.


# 내 풀이
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

def func(start):  # 앞의 숫자와 비교해야하므로 파라미터로 넘겨줌
  if(len(arr) == m):  # s의 길이가 m과 같으면 답 출력
      print(' '.join(map(str,arr)))
      return 

  for i in range(start,n+1):  # 고른 수열은 비내림차순이라는 조건을 만족하기 위해 수열의 앞 요소가 뒷 요소보다 작은 경우가 없도록 범위를 설정
      arr.append(i)  # 수를 더해주고
      func(i)    # 같은 수를 여러 번 사용할 수 있다는 조건을 만족하기 위해 재귀함수 호출시 i+1이 아닌 i를 넘겨줌
      arr.pop()  # 원 상태로 돌리기 위해 pop

func(1)

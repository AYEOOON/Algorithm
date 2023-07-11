# 독일 로또는 {1, 2, ..., 49}에서 수 6개를 고른다.
# 집합 S와 k가 주어졌을 때, 수를 고르는 모든 방법을 구하는 프로그램을 작성하시오.
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있다. 첫 번째 수는 k (6 < k < 13)이고, 다음 k개 수는 집합 S에 포함되는 수이다. S의 원소는 오름차순으로 주어진다.
# 입력의 마지막 줄에는 0이 하나 주어진다. 
# 각 테스트 케이스마다 수를 고르는 모든 방법을 출력한다. 이때, 사전 순으로 출력한다.
# 각 테스트 케이스 사이에는 빈 줄을 하나 출력한다.(중요)
# 다 맞았는데 계속 출력 양식오류가 발생하여 오랫동안 고민 한결과 각 테스트 케이스 사이엔 한줄이 띄워져야한다는 것을 발견하였다.
# 문제를 잘읽자..!
# Asterisk(*): 컨테이너 타입의 데이터를 Unpacking 할 때도 사용된다. 


# 내 풀이(조합 라이브러리 사용)
import sys
from itertools import combinations
input = sys.stdin.readline

while(True):
  num = list(map(int, input().split()))
  arr = []
  
  combi = list(combinations(num[1:], 6))

  for i in combi:
    print(*i)   # 튜플을 정수로 바꿔 출력하는 것이 문제였지만 Asterisk(*)를 통해 해결하였다. 

  if num[0] == 0:
    break
  print()


# 다른 풀이(재귀사용)

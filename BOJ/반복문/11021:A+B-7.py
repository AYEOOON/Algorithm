# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.


t = int(input())

for i in range(1, t+1):
  A, B = map(int,input().split())
  print("Case #%d: %d" % (i, A+B))   # 다음과 같은 문장을 출력할 땐 format을 사용하여 출력한다.
  
  
  
# 다른사람 풀이(1)
import sys  # 파이썬 인터프리터가 제공하는 변수나 함수를 제어할 수 있는 방법을 제공한다.

n = int(input())
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())   # sys모듈을 사용할 때 sys.stdin.readline()을 사용해야 시간초과가 발생하지 않는다.
    print('Case #%d: %d'%(i+1, a + b))

    
# 다른사람 풀이(2)    
import sys

input = sys.stdin.readline   # input에 코드를 추가한다면, input이 sys.stdin.readline의 속도를 갖습니다.

for i in range(n):
  a, b = map(int, input())
  print('Case #%d: %d'%(i+1, a + b))

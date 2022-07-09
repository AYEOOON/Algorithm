# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 이 문제는 EOF(예외처리)를 사용하여 푸는 문제이다.
# 예외처리에 대해 공부하기
# 마지막 풀이에 대해 공부하기

# 내 풀이
import sys

input = sys.stdin.readline

while True:

  try:
    a, b = map(int,input().split())
    print(a+b)

  except:
    break
    
    
# 다름사람 풀이(1)
try:
  while 1:
    a, b = map(int,input().split())
    print(a+b)
except:
  exit()
  
  
# 다른사람 풀이(2)
import sys

for i in sys.stdin:
    a, b = map(int,i.split())
    print(a+b)

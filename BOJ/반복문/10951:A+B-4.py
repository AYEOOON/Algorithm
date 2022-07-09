# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 이 문제는 EOF(예외처리)를 사용하여 푸는 문제이다.
# 예외처리에 대해 공부하기


# 내 풀이(예외 처리를 사용하는 방법)
import sys

input = sys.stdin.readline   # sys.stdin.readline() 을 사용했을 경우
while True:

  try:
    a, b = map(int,input().split())
    print(a+b)

  except:
    break
    
    
# 다름사람 풀이(1)
try:
  while 1:
    a, b = map(int,input().split())  # input() 를 사용했을 경우.(input() 같은 경우, 더이상 값을 읽어오지 못하게 되면 EOFError 가 발생하는데, 그러한 에러를 무시하고 프로그램 정상 종료.)
    print(a+b)
except:
  exit()
  
  
# 다른사람 풀이(2)(예외 처리 없이  sys.stdin.readlines() 를 사용하는 방법)
import sys

lines = sys.stdin.readlines()  # sys.stdin.readlines() 를 쓰게되면 여러번 문자열을 입력받아 저장하게 되는데 미리 저장되어있는 데이터로 반복문을 돌리기때문에 오류가 발생하지 않는다.

for line in lines:
	a,b = map(int,line.split())
    print (a+b)

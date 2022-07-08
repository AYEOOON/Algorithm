# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.


# 내 풀이
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
  a,b = map(int,input().split())
  print('Case #%d: %d + %d = %d'%(i+1, a, b, a+b))
  
  
  
# 다른사람 풀이
import sys
input()
for i,line in enumerate(sys.stdin.readlines()):    # enumerate()함수는 인덱스(index)와 원소를 동시에 접근하면서 루프를 돌릴 수 있는 함수이다.
    A,B=map(int,line.split())
    print(f"Case #{i+1}: {A} + {B} = {A+B}")

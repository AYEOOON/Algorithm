# 숫자와 문자열을 입력받으면 문자열의 각각의 문자를 분리하여 입력받은 숫자만큼 반복해서 출력하는 문제
# 출력할 때는 공백이나 기호의 구분 없이 문자를 붙여서 출력해야 한다.


# 내 풀이

N = int(input())             # 테스트 케이스 수 입력

for _ in range(N):           # 테스트 케이스 수 만큼 for문 반복
  S, P = input().split()     # 첫번째 for문이 반복될 때 숫자와 문자열을 한 줄에 입력받으면 각각 S와 P라는 변수 이름을 지정하여 각각의 값으로 선언
  for i in P:                # 문자열을 iterabl 자리에 입력하여 문자열의 각 문자를 분리하여 변수에 선언
    print(i*int(S), end='')  # print 함수에서 end 파라미터를 이용하지 않을 때는 줄 넘김 기능이 기본값이고 print 함수 안에서 출력할 값이 여러 개인 경우 공백으로 출력 값이 구분된다. 
  print()

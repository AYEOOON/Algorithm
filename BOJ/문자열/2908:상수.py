# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.
# 첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.


# 내 풀이

A, B = input().split()     # input()은 입력받는 모든 것을 문자열로 취급한다.
A = int(A[::-1])
B = int(B[::-1])           # 리스트 슬라이싱은 리스트변수[시작인덱스:종료인덱스:step]으로 이루어진다. step을 이용하면 reverse() 함수를 이용하지 않고도 리스트의 내용을 뒤집을 수 있다.

if A > B:
    print(A)
else:
    print(B)
  
  
  
# reversed 함수를 사용한 풀이

A, B = map(str, input().split())
A1 = ''.join(reversed(A))
B1 = ''.join(reversed(B))
if A1 > B1: print(A1)
else: print(B1)

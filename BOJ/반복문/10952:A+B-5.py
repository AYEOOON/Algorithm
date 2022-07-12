# 두 정수 A와B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.


# 내 풀이
 while True:#  While문을 True로 두어 계속 반복하게 함
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a+b)
    
    
# 다른사람 풀이
import sys

for k in sys.stdin:
    a,b=map(int,k.split())
    if a!=0 and b!=0:
        print(a+b)

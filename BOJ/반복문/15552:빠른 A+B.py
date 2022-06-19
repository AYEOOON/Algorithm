# 1라인의 import sys 코드는 sys를 포함하겠다는 것으로 sys.stdin.readline()을 사용할 수 있도록 하는 코드이다.
# 사용자가 원하는 갯수를 받는 input 변수를 지정해주고, for문을 inp값에서 하나 뺀 값까지 반복해 a와 b를 입력받고, 둘을 더한 값을 출력해준다.



import sys
 
inp = int(input())
for i in range(inp):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)

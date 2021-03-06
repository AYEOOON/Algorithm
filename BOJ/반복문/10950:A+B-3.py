# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)


# 내 풀이
T = int(input())       # T를 입력받음   
for i in range(T):
    A, B = map(int,input().split())
    print(A+B)

    
# 다른사람 풀이    
import sys

input()
s = list(sum(map(int, n.split())) for n in sys.stdin)

for n in s:
  print(n)
    
    
# range안에서 단일로 숫자를 넣게 되면 해당 횟수만큼 for문이 돌게 된다. 
# 자는 따로 사용하지 않으므로 _을 넣어주면 된다. 만약 for와 in 사이에 아무것도 넣지 않게 되면 오류가 나므로 유의해야 한다. 

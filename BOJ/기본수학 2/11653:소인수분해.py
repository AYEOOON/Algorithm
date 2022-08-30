# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
# N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다. 


# 내 풀이

import sys
input = sys.stdin.readline

N = int(input())
m = 2

while N != 1:   # N이 1이 아닐 경우  
  if N%m == 0:  # N이 2로 먼저 나누었을 때 0인 경우
    print(m)
    N = N//m 
  else:
    m += 1
    
    
# 다른사람 풀이

n = int(input())
i = 2
r = int(n ** 0.5)

while i <= r:
    while not n % i:
        print(i)
        n //= i
    i += 1
if n > 1:
    print(n)

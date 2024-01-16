"""
어떤 수와 그 수의 숫자 순서를 뒤집은 수가 일치하는 수를 팰린드롬이라 부른다. 
예를 들어 79,197과 324,423 등이 팰린드롬 수이다.

어떤 수 N (1 ≤ N ≤ 1,000,000)이 주어졌을 때, N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서, 가장 작은 수를 구하는 프로그램을 작성하시오.
"""
"""
1. 소수를 판별하는 함수 구현
2. N부터 1,000,000 까지의 반복문을 돌림
3. 만약에 num이 1이면 예외처리(이 부분이 오류의 원인)
4. 팰린드롬 수이고, 소수이면 result는 num, 반복문 중지
5. 만약에 N이 1,000,000이라면, 1,000,000이 넘는 수 중 팰린드롬 수이면서 소수인것을 출력(이 부분도 오류의 원인이었다.)
"""

# 내 풀이
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def sosu(n):  # 소수 판별 함수
  for i in range(2, int(n**0.5)+1):
    if n%i == 0:
      return False
  return True  # 들여쓰기를 주의하자!
    
N = int(input())
result = 0

for num in range(N, 1000001):
  if num == 1:  # num이 1이라면 예외처리
    continue
  if str(num) == str(num)[::-1]:  # 팰린드롬 수라면
    if sosu(num) == True:  # 소수라면
      result = num 
      break

if result == 0:  # 1,000,000일 때
  result = 1003001

print(result)

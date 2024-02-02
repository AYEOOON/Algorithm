"""
IQ Test의 문제 중에는 공통된 패턴을 찾는 문제가 있다. 수열이 주어졌을 때, 다음 수를 찾는 문제이다.
항상 모든 답은 구하는 규칙은 앞 수*a + b이다. 그리고, a와 b는 정수이다.

수 N개가 주어졌을 때, 규칙에 맞는 다음 수를 구하는 프로그램을 작성하시오.
"""
"""
- N이 1이라면 무조건 A출력
- N이 2라면 
  - x0과 x1이 같으면 제일 처음 수 출력
  - 같지않으면 A출력
- N이 3이상이라면
 - 만약 x1-x0이 0이 아니라면 
   => a는 (x2-x1)/(x0-x1)
 - 0이라면 
   => a는 0
 - b는 x1-x0*a
 - 순차적으로 숫자들이 ax0 + b로 구성되어있는지 확인
   - 맞으면 마지막 숫자에 a,b 대입
   - 틀리면 B출력
"""

# 내 풀이
import sys
input = sys.stdin.readline

N = int(input())

nums = list(map(int,input().split()))

if N == 1:
  print("A")
if N == 2:
  if nums[0] == nums[1]:
    print(nums[0])
  else:
    print("A")

if N >= 3:
  if (nums[1] - nums[0]) != 0:
    a = (nums[2] - nums[1]) // (nums[1] - nums[0])
  else:
    a = 0
    
  b = nums[1] - nums[0]*a
    
  for i in range(2, len(nums)):
    if nums[i] == nums[i-1]*a+b:
      answer = nums[-1] * a + b
    else:
      answer = "B"
      break  # 이자리에 바로 exit()를 사용해도 무방

  print(answer)

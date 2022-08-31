# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
# 한번더 봐야할 문제


# 내 풀이

import sys
import math
input = sys.stdin.readline

M, N = map(int,input().split())

I = [True for i in range(N+1)]              # 처음엔 모든 수가 소수(True)인 것으로 초기화

for i in range(2, int(math.sqrt(N)) + 1):   # 2부터 n의 제곱근까지
  if I[i] == True:                          # i가 소수인 경우 (남은 수인 경우)
    j = 2                                   # i를 제외한 1의 모든 배수를 지우기
    while i * j <= N:
      I[i * j] = False
      j += 1

for i in range(M, N+1):                    # 모든 소수 출력
  if I[i]:
    if i != 1:
      print(i)

# 100보다 작은 m에 대해서 m = a*b 라면, a와 b 중 적어도 하나는 100의 제곱근인 10보다 같거나 작아야한다.
# 100보다 작은 소수를 찾을 때, 제곱근은 10보다 작은 수의 배수만 검사해도 전수조사가 가능하다.

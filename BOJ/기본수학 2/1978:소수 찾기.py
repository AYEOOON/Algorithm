# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
# 소수를 판별하기 위해서 각 숫자가 1부터 해당 숫자까지 숫자 범위에서 1과 자기 자신을 제외한 수로 나누어 떨어지는 여부를 if조건식을 이용하였다. 


# 내 풀이

import sys
input = sys.stdin.readline

N = int(input())                         # 숫자의 갯수 N을 입력받음
numbers = map(int,input().split())       # 숫자들을 공백으로 구분하여 입력받음

sosu = 0

for num in numbers:                      # numbers 변수에 있는 숫자들을 하나씩 num 변수에 선언
  error = 0                              # error 변수는 첫 번째 for문이 시작될 때마다 0으로 선언
  if num > 1 :
    for i in range(2, num):              # for문의 숫자 범위는 2부터 num-1 까지이다.
      if num % i == 0:
        error += 1                       # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
    if error == 0:
      sosu += 1
      
print(sosu)


# 다른 방법(언니의 풀이)

N = int(input())
sosu = 0                        # 소수가 몇 개인지 count                 

a = map(int, input().split())

for i in a:                     # a 안에 입력받은 요소를 for문 변수 i에 선언
  if 1 < i:                     # i가 1보다 클 경우 if문
    x = 0                       # 변수 x는 for문이 한번 돌 때 마다 0으로 초기화
    
    for j in range(2, i):       # 2부터 변수 i-1까지를 범위로 하는 for문 변수 j
      if i%j == 0:              # j와 i를 나누어 0으로 나누어 떨어질 경우를 확인
        x += 1                  # 나누어 떨어진다면 소수가 아니므로 변수 x에 +1

    if x == 0:                  # x==0 일 경우 1과 자기 자신을 제외한 숫자로는 나누어 떨어지지 않는 것을 의미
      sosu += 1                 # sosu 변수에 +1

      
# 다른방법(에라토스테네스의 체 사용하기)

def prime(numbers, l):
  for i in range(2, int(l ** 0.5) + 1):
    if not numbers[i]:
      for j in range(i**2, l, i):
        numbers[j] = 1

  return numbers

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


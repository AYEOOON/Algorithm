# 자연수 N과 K가 주어졌을 때, 이항계수를 구하는 프로그램을 작성하는 문제

# 내 풀이(재귀함수 사용)
import sys
input = sys.stdin.readline


def factorial(n):
  result = 1
  if n > 0:
    result = n * factorial(n-1)
  return result

n, k = map(int,input().split())
print(factorial(n)//(factorial(k) * factorial(n-k)))


# 개선한 내풀이
def fac(n):
  if n==0:
    return 1
  else:
    return n*fac(n-1)
n , k = map(int, input().split())
print(int(fac(n)/(fac(k)*fac(n-k))))


# 다른사람 풀이
n, k = map(int, input().split())

a = 1
b = 1

for i in range(n, n-k, -1):
    a *= i

for j in range(1, k+1):
    b *= j

print(a//b)

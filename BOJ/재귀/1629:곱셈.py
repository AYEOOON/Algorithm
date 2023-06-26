# 자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.
# 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.
# 첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
# 이 문제를 풀기위해서는 나머지 분배 법칙과 지수법칙을 알아야한다. 
# 지수 법칙 -> A^m+n = A^m x A^n
# 나머지 분배 법칙 -> (AxB)%C = (A%C) *(B%C) % C
# 예를 들어, 2^32라면 2를 32번 곱하는 방법도 있지만, 
# (2^16)^2로 해서 풀면 2를 16번 곱한 것을 다시 2번 곱하니 17번의 연산만으로 끝낼 수 있어 시간이 훨씬 적게 든다. 
# 이를 계속 해보면 {(2^8)^2}^2 이렇게 풀면 10번만에, [{(2^4)^2}^2]^2 이렇게 풀면 7번만에 끝낼 수 있어 시간이 획기적으로 주는 것이다.

# 풀이
import sys
a,b,m = map(int,sys.stdin.readline().split())

def multi(a,b):
  if (b == 1):
    return a%m

  val = multi(a, b//2)
  if(b%2==0):  # b가 짝수일때 
    return val*val%m

  elif(b%2==1):  # b가 홀수일때
    return val*val*a%m

print(multi(a,b))


# 다른사람 풀이1
print(pow(*map(int,input().split())))


# 다른사람 풀이2
from sys import stdin
input = stdin.readline

def solve():
    a, b, c = map(int, input().split())

    print(pow(a, b, c))

if __name__ == '__main__':
    solve()

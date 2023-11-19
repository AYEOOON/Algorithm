# 피보나치 알고리즘에서 n이 주어졌을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

# 피보나치 알고리즘 관련 문제는 다이나믹 프로그래밍으로 풀어야함
# 예제를 몇개 풀어보면
# 0 :  1 0
# 1 :  0 1
# 2 :  1 1
# 3 :  1 2
# 4 :  2 3
# 5 :  3 5
# 이러한 규칙이 나온다
# zero(n) = zero(n-1) + zero(n-2) 라는 점화식을 얻을 수 있다. 

# 내 풀이
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
  zero_cnt = [1,0]
  one_cnt = [0,1]
  t = int(input())
  if t > 1:
    for j in range(2,t+1):
      zero_cnt.append(zero_cnt[j-1]+zero_cnt[j-2])
      one_cnt.append(one_cnt[j-1]+one_cnt[j-2])

  print(zero_cnt[t], one_cnt[t])


# 다른사람 풀이
t = int(input())
def fib(n):
    a,b = 1,0
    c,d = 0,1
    for i in range(n):
        a,b,c,d = c,d,a+c,b+d
    return a,b

for i in range(t):
    a,b = fib(int(input()))
    print(a,b)

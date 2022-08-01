# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
# for와 if를 같이 쓰는 문제
# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.


# 내 풀이
import sys

input = sys.stdin.readline  

n, x = map(int,input().split())
a = list(map(int,input().split()))
for i in range(n):
  if a[i] < x:
    print(a[i], end=' ')

    
    
# 다른사람 풀이(1)
_, n = map(int, input().split())
print(' '.join(map(str, [i for i in list(map(int, input().split())) if i < n]))) 


# 다른사람 풀이(2)
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in A:                 #for문으로 수열의 개수 N개를 먼저 지정하여 수열 A가 N개의 정수로 구성됨을 상기시켰다.
    if i < X:
        print(i, end=" ")

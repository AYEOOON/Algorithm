# N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.
# 탐색의 제약 조건은 중복을 제외한다는 점만 신경쓰면 된다. 
# 탐색 종료 조건에서 합이 S인지만 확인하면 된다. 
# 종료조건에서 return을 사용하여 계속 런타임에러가 발생하였다. 
# 종료조건에 len(arr) > 0이 조건을 추가하고, return을 없애 해결하였다.


# 내 풀이
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
num = list(map(int, input().split()))
arr = []
cnt = 0

def func(start):  # 입력받은 수열을 사용해야하므로, start부터 다음 탐색을 진행하고 있다. 
  global cnt
  if(sum(arr) == s and len(arr) > 0):
      cnt += 1
    
  for i in range(start, n):
      arr.append(num[i])
      func(i+1)
      arr.pop()

func(0)
print(cnt)



# 수열을 이용한 풀이
import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
    comb = combinations(arr, i)

    for x in comb:
        if sum(x) == s:
            cnt += 1

print(cnt)

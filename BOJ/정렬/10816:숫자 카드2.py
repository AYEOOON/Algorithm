# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 
# 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
# N개의 카드 중에서 입력한 M의 숫자를 가진 카드가 몇개 있는지 찾는 문제
# count 함수를 사용하면 시간초과가 발생
# count sort를 사용하였다. 

# 내 풀이
import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
nums = list(map(int, input().split()))

dic = {}

for i in cards:
  if i in dic:  # 카드의 갯수 누적
    dic[i] += 1
  else: # 새로운 카드 입력
    dic[i] = 1

arr = []

for j in nums:
  result = dic.get(j)  # 딕셔너리의 값을 가져오는 함수
  if result == None:
    arr.append(0)
  else:
    arr.append(result)
    
print(*arr)  # 리스트를 unpacking할 때 사용하는 *


# 다른사람 풀이(Collection 라이브러리의 Counter 함수사용)
from sys import stdin
from collections import Counter
_ = stdin.readline()
N = stdin.readline().split()
_ = stdin.readline()
M = stdin.readline().split()

C = Counter(N)  # 리스트 N을 Counter에 넣으면 N의 요소들의 숫자를 센 Dictionary자료형이 출력
print(' '.join(f'{C[m]}' if m in C else '0' for m in M))

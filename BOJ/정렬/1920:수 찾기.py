# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.


# 내 풀이(이분탐색)
N = int(input())
A_nums = list(map(int, input().split()))

M = int(input())
B_nums= list(map(int, input().split()))

A_nums.sort()  # 이분 탐색을 위해서 집합 N을 먼저 정렬

def binary_search(i):
  start = 0  # 시작과 끝 지점의 index를 지정
  end = N-1
  
  while start<=end:
    mid = (start + end) // 2  # 시작 인덱스와 끝 인덱스를 사용해서 중간 지점의 인덱스를 구함

    # 중간 지점의 값과 element를 비교
    if A_nums[mid] == i: # 동일한 값이면 찾음
      return True
    elif A_nums[mid] < i:  # 값이 크다 => 중간보다 윗부분에서 탐색
      start = mid + 1
    else:  # 값이 작다 => 중간보다 작은 부분에서 탐색
      end = mid - 1  # 위 과정을 확인할 리스트가 없을 때까지 계속해서 반복

for i in range(M):
  if binary_search(B_nums[i]):
    print(1)
  else:
    print(0)


# 다른사람 풀이
N = int(input())
# 집합 N을 Set 함수를 사용해서 빠르고 쉽게 M집합의 요소들의 포함 여부를 확인할 수 있다.
A = set(map(int, input().split()))	# 탐색 시간을 줄이기 위해 set으로 받음
M = int(input())
arr = list(map(int, input().split()))

for num in arr:		# arr의 각 원소별로 탐색
    print(1) if num in A else print(0)	# num이 A 안에 있으면 1, 없으면 0 출력

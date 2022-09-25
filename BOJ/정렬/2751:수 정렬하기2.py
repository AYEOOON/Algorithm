# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 시간 복잡도가 O(nlogn)인 정렬 알고리즘으로 풀 수 있습니다. 예를 들면 병합 정렬, 힙 정렬 등이 있다.
# python3으로 채점하면 오류가남. pypy3으로 채점


# 내 풀이(sort 사용)

N = int(input())
arr = []

for i in range(N):
  arr.append(int(input()))

arr.sort()
for i in arr:
  print(i)
  
  
  
# 다른 풀이(merge sort(병합정렬)사용)
# https://eunhee-programming.tistory.com/105

def merge_sort(array):
  if len(array)<=1:
    return array
  mid = len(array)//2

  #left는 array리스트의 인덱스 0부터 mid전까지
  left = merge_sort(array[:mid]) 

  #right은 array리스트의 인덱스 mid부터 끝까지
  right = merge_sort(array[mid:])

  i, j, k = 0, 0, 0
  arr = []
  
  #둘중 하나조건에 부합하지 않을경우 while문 빠져나감 
  while i < len(left) and j < len(right): 
    if left[i] < right[j]:
      arr.append(left[i])
      i+=1
    else:
      arr.append(right[j])
      j+=1

#while문 빠져 나온 후, left혹은 right에 남은 요소들 arr에 넣어주기
  arr += left[i:] 
  arr += right[j:]
 
  return arr

N = int(input())
arr=[]

for _ in range(N):
  arr.append(int(input()))

arr = merge_sort(arr)

for i in arr:
  print(i)

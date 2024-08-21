"""
정수 n, left, right가 주어집니다. 다음 과정을 거쳐서 1차원 배열을 만들고자 합니다.

  1. n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
  2. i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
    - 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
  3. 1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
  4. 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.

정수 n, left, right가 매개변수로 주어집니다. 주어진 과정대로 만들어진 1차원 배열을 return 하도록 solution 함수를 완성해주세요.
"""

# 2차원 배열을 만들어 모든 숫자를 채운 뒤 평면 배열로 만들어 해결해면 시간초과 발생
# left~ right 사이의 값만 구하여야한다.
# 2차원 배열의 x,y 중 큰값이 그 자리의 값이 되는 것을 이용하고, left와 right를 n와의 몫과 나머지를 구하여 범위를 구함


# 내 풀이
def solution(n, left, right):
    arr = []
    
    for i in range(right-left+1):
        arr.append(max((left+i)//n+1, (left+i)%n+1))
        
    return arr


# 다른사람 풀이
def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer

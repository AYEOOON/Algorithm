# 정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성하는 문제


# 내 풀이

def solution(array):
  array.sort()              # 매개변수로 받은 배열을 우선 오름차순으로 정렬
  nums = len(array)//2      # 편의를 위해 배열의 중간 인덱스를 nums에 저장
  return array[nums]        # 중간 인덱스를 리턴



# 다른 사람 풀이

def solution(array):
    return sorted(array)[len(array) // 2]

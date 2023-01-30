# 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 
# 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.
# 어려움..


# 풀이1
# duque는 스택과 큐의 기능을 모두 가진 객체로 출입구를 양쪽에 가지고 있다. 
# https://dongdongfather.tistory.com/72

from collections import deque        # deque를 사용하기위해 deque를 import해준다.

def solution(numbers, direction):
  numbers = deque(numbers)           # number를 deque로 만든다.
  if directuon == "right":           # right면 rotate()함수를 이용하여 오른쪽으로 1칸 이동한다.
    numbers.rotate(1)
  elif direction == "left":          # left 면 rotate()함수를 이용하여 왼쪽으로 1칸 이동 한다.
    numbers.rotate(-1)
    
   return list(numbers)              # deque를 사용하면 deque형으로 바뀌기 때문에 list로 변환 해주고 return 해준다.

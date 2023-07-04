# 상자의 가로, 세로, 높이가 저장되어있는 배열 box와 주사위 모서리의 길이 정수 n이 매개변수로 주어졌을 때, 상자에 들어갈 수 있는 주사위의 최대 개수를 return 하도록 solution 함수를 완성해주세요.


# 내 풀이

def solution(box, n):
    return (int(box[0]//n)*int(box[1]//n)*int(box[2]//n))
  
  
# 다른사람 풀이
# math.prod() : ()안에 있는 모든 iterable 요소들의 곱을 구한다.
# box안에 있는 모든 값 v들을 n으로 나눈 값의 몫을 모두 곱하는 값을 구한다.

import math

def solution(box, n):
    return math.prod(map(lambda v: v//n, box))

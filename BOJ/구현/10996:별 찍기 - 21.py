""" 
예제를 보고 규칙을 유추한 뒤에 별을 찍어보세요.

입력
1

출력
*

입력
3

출력
*
 *
*
 *

"""

# 내 풀이
import math

n = int(input())

for _ in range(n):

  print('* ' * (math.floor((n-1)/2)+1))
  print(' *' * math.ceil((n-1)/2))


# 다른사람 풀이
import sys
input = sys.stdin.readline

N = int(input().rstrip())

star = '*'
space = ' '

for i in range(2*N):
    temp = ''
    for j in range(N):
        if i % 2 == 0:    # 짝수행일 때
            if j % 2 == 0:
                temp += star
            else:
                temp += space
        else:    # 홀수행일 때
             if j % 2 == 0:
                 temp += space
             else:
                 temp += star
    if temp != ' ':    # 공백 하나로 이루어진 문자열이 아닌 경우에만 출력
        print(temp)

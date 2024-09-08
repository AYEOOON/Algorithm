"""
Elly는 예상치 못하게 프로그래밍 대회를 준비하는 학생들을 가르칠 위기에 처했다. 
대회는 정확히 3명으로 구성된 팀만 참가가 가능하다. 그러나 그녀가 가르칠 학생들에게는 큰 문제가 있었다. 
코딩 실력이 좋으면 팀워크가 떨어지고, 팀워크가 좋을수록 코딩 실력이 떨어진다. 그리고 출전하고자 하는 대회는 코딩 실력과 팀워크 모두가 중요하다.

Elly는 그녀가 가르칠 수 있는 모든 학생들의 코딩 실력을 알고 있다. 
각각의 코딩 실력 Ai는 -10000부터 10000 사이의 정수로 표시되어 있다. 
그녀는 팀워크와 코딩 실력이 모두 적절한 팀을 만들기 위해, 세 팀원의 코딩 실력의 합이 0이 되는 팀을 만들고자 한다. 
이러한 조건 하에, 그녀가 대회에 출전할 수 있는 팀을 얼마나 많이 만들 수 있는지를 계산하여라.

N명의 학생들의 코딩 실력 Ai가 -10000부터 10000사이의 정수로 주어질 때, 합이 0이 되는 3인조를 만들 수 있는 경우의 수를 구하여라.
"""
"""
처음에 조합을 이용하여 학생들을 입력 받은 후 3인조가 될 수 있는 경우를 만들어 합이 0이 되면 팀수를 증가시키는 방법을 이용하였지만 메모리초과가 발생하였다. 
그래서 다른사람의 아이디어를 참고하여 풀었다. 
1. 학생들을 입력받고 정렬을 한다. 
2. 학생의 수 만큼 반복을 한다. 
 - 이분탐색 (left = i+1, right = 학생수-1)
 - result : 세 수의 합
 - 0보다 크면 right-1
 - 0보다 작거나 같으면 left + 1
 (중복을 허용하기 때문에 0일 경우 팀 수에 중복되는 길이를 더하기)
3. 팀 수 출력
"""

# 내 풀이
import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
students = list(map(int,input().split()))  # 학생입력
students = sorted(students) # 정렬

team = 0

for i in range(len(students)):  # 학생들을 훑기
  left = i+1
  right = len(students)-1
  while(left < right):
    result = students[i] + students[left] + students[right]
    if result > 0:
      right -= 1
    else:
      if result == 0:
        if students[left] == students[right]:
          team += (right - left)
        else:
          idx = bisect_left(students, students[right])  # *bisect : team에 더해줄 때, 중복되는 수의 갯수를 쉽게 구해주는 함수
          team += (right - idx+1)
      left += 1

print(team)

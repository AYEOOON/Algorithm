# 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.
# 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.
# 출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.
# 1부터 30까지의 리스트를 생성한 후 입력받은 수를 리스트에서 제거한다. 리스트에 남은 값이 과제를 제출하지 않은 학생의 출석번호이다. 



# 내 풀이
import sys
input = sys.stdin.readline

students = [i for i in range(1,31)]    # 1부터 30까지의 리스트를 생성

for _ in range(28):
  handout = int(input())
  students.remove(handout)     # 입력받은 숫자를 리스트에서 제거

print(min(students))
print(max(students))



# 다른 사람 풀이

x=list(map(int,range(31)))
del x[0]
for i in range(28):
    x.remove(int(input()))
for j in x:
    print(j)

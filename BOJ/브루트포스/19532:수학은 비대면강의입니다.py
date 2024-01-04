"""
수현이는 4차 산업혁명 시대에 살고 있는 중학생이다.
코로나 19로 인해, 수현이는 버추얼 학교로 버추얼 출석해 버추얼 강의를 듣고 있다. 
수현이의 버추얼 선생님은 문자가 2개인 연립방정식을 해결하는 방법에 대해 강의하고, 다음과 같은 문제를 숙제로 냈다.

다음 연립방정식에서 
ax + by = c와 
dx + ey = f의 값을 계산하시오.

4차 산업혁명 시대에 숙제나 하고 앉아있는 것보다 버추얼 친구들을 만나러 가는 게 더 가치있는 일이라고 생각했던 수현이는 이런 연립방정식을 풀 시간이 없었다. 
다행히도, 버추얼 강의의 숙제 제출은 인터넷 창의 빈 칸에 수들을 입력하는 식이다. 각 칸에는 -999이상 999이하의 정수만 입력할 수 있다. 
수현이가 버추얼 친구들을 만나러 버추얼 세계로 떠날 수 있게 도와주자.
"""

# 내 풀이
import sys
input = sys.stdin.readline

a,b,c,d,e,f = map(int,input().split())
ans = []

for x in range(-999, 1000):  # 범위는 항상 N-1까지임을 기억하자!
  for y in range(-999,1000):
    if (a*x) + (b*y) == c and (d*x) + (e*y) == f:
      ans = [x,y]

print(*ans)

# 다른사람 풀이
# 가감법을 이용
# X자 모양으로 수를 곱한 뒤 나눠주면 쉽게 x와 y를 구할 수 있다. 
a, b, c, d, e, f = map(int, input().split())
x = (c*e-b*f)//(a*e-b*d)
y = (c*d-a*f)//(b*d-a*e)
print(x, y)

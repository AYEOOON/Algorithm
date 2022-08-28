# 설탕의 무게를 나타내는 숫자 N이 입력되면 3 킬로그램과 5 킬로그램으로 된 봉지에 나누어 담아서 가장 적은 수의 봉지 개수를 출력하는 문제이다.
# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 설탕을 나눠 담을 때 정확하게 n이 될 수 없는 경우에는 -1을 출력한다.
# while 반복문을 사용하여 5의 배수가 될 때까지 설탕의 무게에서 3씩 빼가는 방식으로 코드를 작성.
# 딱 나누어 떨어지지 않을 때는 while-else문을 활용하여 -1을 출력하도록 함



# 내 풀이

import sys
input = sys.stdin.readline

sugar = int(input())

bag = 0

while sugar >= 0:          # while문은 sugar의 갯수가 0보다 크거나 같을 때까지만 반복
  if sugar % 5 == 0:       # 5의 배수일 경우
    bag += (sugar//5)      # 5로 나눈 몫을 구해야 정수가 됨
    print(bag)
    break
  sugar -= 3
  bag += 1                 # 5의 배수가 될 때까지 설탕 -3, 봉지 +1
else:
  print(-1)

# 다른사람 풀이

n = int(input())

a = n//5
b = n%5
c = 0

while a>=0:
    if b%3 == 0:
        c = b//3
        
        break
    a -= 1
    b += 5
        
if b%3 == 0:
    print(a+c)
else:
    print(-1)

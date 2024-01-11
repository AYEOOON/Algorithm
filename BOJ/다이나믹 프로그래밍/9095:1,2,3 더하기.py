"""
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
"""
"""
숫자들의 합만 봤을 땐 규칙이 보이지 않았지만, 방법의 갯수를 보니 규칙이 보였다.
1부터 7까지
1,2,4,7,13,24,44 를 보면 앞에 3개를 더한 값이 n번째 수를 나타내는 것을 볼 수 있다. 
따라서 
a[n] = a[n-1] + a[n-2] + a[n-3]
이라는 식을 도출할 수 있다. 
"""

# 내 풀이
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  arr = []
  n = int(input())
  for i in range(n+1):
    if i == 0:
      arr.append(0)
    elif i == 1:
      arr.append(1)
    elif i == 2:
      arr.append(2)
    elif i == 3:
      arr.append(4)
    else:
      arr.append(arr[i-1] + arr[i-2] + arr[i-3])

  print(arr[n])


# 다른사람 풀이
T = int(input())
a = [int(input()) for _ in range(T)]
c = [0]*(11)
c[1] = 1
c[2] = 2
c[3] = 4
for i in range(4, 11):
    c[i] = c[i-1] + c[i-2] + c[i-3]
for b in a:
    print(c[b])

# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.
# 첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다. 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다. 이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.
# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes를 출력한다. 일치하지 않는다면 No를 출력한다.

# 내 풀이

x = int(input())
n = int(input())

for i in range(n):
  p, m = map(int,input().split())

  x -= (p*m)

print("Yes" if x == 0 else "No")


# 함수를 이용한 풀이

import sys

input = sys.stdin.readline

# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 확인하는 함수
def solve(target, datas) -> str:
    return 'Yes' if target == sum([x[0] * x[1] for x in datas]) else 'No'

if __name__ == '__main__':
    x = int(input())  # x: 영수증에 적힌 총 금액
    n = int(input())  # n: 영수증에 적힌 구매한 물건의 종류의 수
    datas = [list(map(int, input().split())) for _ in range(n)]

    print(solve(x, datas))

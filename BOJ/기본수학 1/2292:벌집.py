# 랜덤으로 숫자 N이 주어질 때 1이 있는 벌집 위치에서 숫자 N까지 거쳐가는 단계의 수를 찾아내는 문제
# 벌집의 개수가 6배수로 증가하여 이 점을 이용하여 while문을 이용하여 풀었다.
# while문은 증가하는 숫자가 입력받은 수인 N에 도달할 때까지만 반복하도록 하였고, 반복되는 동안 반복횟수를 카운트아여 마지막에 출력


# 내 풀이

import sys
input = sys.stdin.readline

N = int(input())

berzip = 1               # 벌집의 갯수
cnt = 1                  # 반복 횟수

while N > berzip:        # berzip 변수가 n보다 커지는 순간 반복문은 종료
  berzip += 6 * cnt      # berzip 변수에는 6의 배수를 더해서 점차 증가하게 만듦
  cnt += 1               # while문이 반복되는 동안 1씩 증가
print(cnt)               # 반복횟수 출력



# 다른사람 풀이

n = int(input())
k = (n-1)/6

i=0
while i*(i+1)/2<k:
    i+=1

print(i+1)

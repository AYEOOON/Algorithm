# 무한히 큰 배열에 적힌 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하는 문제.
# 짝수라인은 시작점에서 끝점으로 갈수록 분자가 1씩 늘어가고 분모가 1씩 감소하며
# 홀수라인은 시작점에서 끝점으로 갈수록 분자가 1씩 줄어들고 분모가 1씩 늘어난다.
# 구하고자 하는 수가 몇번째 라인에 있는지, 그 중에서 몇 번째 인덱스에 있는지를 알면됨.


# 풀이1

n = int(input())

line = 0
end = 0
while n > end:
    line += 1
    end += line

diff = end - n
if line%2 == 0: #짝수 라인 일때
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print("%d/%d"%(top,bottom))


# 풀이2

N = int(input())
line = 1            # 대각선의 번호

while N > line :    # 입력받은 N이 대각선보다 클 경우 반복하여 입력받은 N이 해당하는 대각선 번호를 구함
  N -= line         # 예를 들어, N이 14일 때 N = 14, 13, 11, 8, 4가 되고
  line += 1         # line은 1, 2, 3, 4, 5가 된다.

if line % 2 == 0:   # 대각선이 짝수번째 일 경우 
  i = N             # 분자
  j = line-N+1      # 분모

else:               # 대각선이 홀수번째 일 경우   
  i = line-N+1      
  j = N

print(i ,'/', j, sep="")

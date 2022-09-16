# O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다. OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스마다 점수를 출력한다.

# 내 풀이

C = int(input())

for _ in range(C):
  N = input()
  count = 0
  result = 0            # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다.

  for j in N:
    if j == 'X':        # 만약 for문 변수 j가 "x"를 만난다면 count를 0으로 초기화
      count = 0         # 다시 그 다음 "O"를 만날 때 다시 1부터 count를 셀 수 있도록 함
      continue

    count += 1          # 'O'가 연속되면 점수가 1점씩 커진다.
    result += count     # sum_score = sum_score + score

  print(result)

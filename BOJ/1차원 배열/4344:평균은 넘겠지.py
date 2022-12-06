# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다. 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

# 내 풀이

n = int(input())

for _ in range(n):
  num = list(map(int,input().split()))
  avg = sum(num[1:])/num[0]              # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
  cnt = 0

  for score in num[1:]:                  # for문으로 점수 각각을 score 변수에 선언
    if score > avg:
      cnt += 1                           # 평균 이상인 학생 수 (평균보다 큰 점수인 경우 1씩 더함)

  rate = cnt/num[0]*100
  print(f'{rate:.3f}%')                  # f-string 표기법으로 문자열을 작성하면 { } 중괄호를 이용해서 변수를 삽입할 수 있다.

  
  
# 위 코드에서 count변수를 0으로 초기화하고 for 구문을 다음과 같이 한 줄로 나타낼 수 있다.
count = sum([1 for i in score[1:] if i > a])

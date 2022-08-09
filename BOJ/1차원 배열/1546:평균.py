# 자기 점수 중에 최댓값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다. 새로운 평균을 구하는 프로그램을 작성하시오.
# 첫째 줄에 시험 본 과목의 개수 N이 주어진다. 둘째 줄에 세준이의 현재 성적이 주어진다.
# 첫째 줄에 새로운 평균을 출력한다. 


# 내 풀이

n = int(input())                           # 과목수

x = list(map(int,input().split()))
max_score = max(x)

new_score = []
for score in x:
  new_score.append(score/max_score*100)    # 새로운 점수 생성
test_avg = sum(new_score)/n
print(test_avg)


# 다른사람 풀이

n = int(input())
s = [int(x) for x in input().split()]

ss = sum(s)
print(ss/max(s)*100/n)

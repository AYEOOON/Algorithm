# 영화 감독 숌은 영화 제목에 종말의 수를 넣어 만드려고 한다. 
# 종말의 수란 어떤 수에 6이 적얻 3개 이상 연속으로 들어가는 수를 말한다. 
# 제일 작은 종말의 수는 666이며, 그다음은 1666, 2666,,,,
# 숌이 만든 N번째 영화의 제목이 들어간 수를 출력하는 프로그램을 작성하는 문제

# 이 문제의 경우 브루트포스를 사용하여 풀었다. 
# 모든 경우를 다 넣고 조건에 맞으면 정답을 출력한다. 

# 내 풀이
import sys
input = sys.stdin.readline

N = int(input())  # N입력

first = 666  # 첫번째 종말의 수
cnt = 1  

while (cnt != N):  # cnt가 N과 같지 않을 때 반복
  first += 1  # 첫번째 종말의 수에서 1씩 증가
  if '666' in str(first): # 만약 first에 666이 존재하면, 문자열로 바꾸어 비교하는 것이 중요하다.
    cnt += 1  # cnt증가

print(first)


# 다른사람 풀이
# 코드의 길이는 길지만, 시간은 짧음
N = int(input())
li = []
n = 0
while len(li) < N:
    if not n%10 == 6:
        li.append(n*1000+666)
    elif (n//10)%100 == 66:
        for k in range (1000):
            li.append(n*1000+k)
    elif (n//10)%10 == 6:
        for j in range (100):
            li.append(n*1000+600+j)
    else:
        for i in range (10):
            li.append(n*1000+660+i)
    n += 1

print (li[N-1])

# 어떤 문제의 난이도는 그 문제를 푼 사람들이 제출한 난이도 의견을 바탕으로 결정한다. 난이도 의견은 그 사용자가 생각한 난이도를 의미하는 정수 하나로 주어진다. solved.ac가 사용자들의 의견을 바탕으로 난이도를 결정하는 방식은 다음과 같다.

# 아직 아무 의견이 없다면 문제의 난이도는 0으로 결정한다.
# 의견이 하나 이상 있다면, 문제의 난이도는 모든 사람의 난이도 의견의 30% 절사평균으로 결정한다.

# 30% 절사평균의 경우 위에서 15%, 아래에서 15%를 각각 제외하고 평균을 계산한다. 따라서 20명이 투표했다면, 가장 높은 난이도에 투표한 3명과 가장 낮은 난이도에 투표한 3명의 투표는 평균 계산에 반영하지 않는다는 것이다.
# 제외되는 사람의 수는 위, 아래에서 각각 반올림한다. 25명이 투표한 경우 위, 아래에서 각각 3.75명을 제외해야 하는데, 이 경우 반올림해 4명씩을 제외한다.
# 마지막으로, 계산된 평균도 정수로 반올림된다. 절사평균이 16.7이었다면 최종 난이도는 17이 된다.
# 사용자들이 어떤 문제에 제출한 난이도 의견 목록이 주어질 때, solved.ac가 결정한 문제의 난이도를 계산하는 프로그램을 작성하시오.

# 주의할점
# 단순히 round함수를 사용하면 런타임에러가 발생한다.
# N이 0이면 0을 출력해준다. 
# 절사평균 -> 정렬 -> 슬라이싱의 과정을 거친다. 

# 내 풀이
import sys
input = sys.stdin.readline

def roundUP(num):
  return int(num)+1 if num-int(num) >= 0.5 else int(num)

N = int(input())
arr = []

if (N!=0):
  for i in range(N):
    arr.append(int(input()))
  
  arr = sorted(arr)
  new_arr = arr[roundUP(N*0.15):len(arr)-roundUP(N*0.15)]
  print(roundUP(sum(new_arr)/len(new_arr)))

else:
  print(0)


# 다른사람의 풀이
# 파이썬에서 반올림 함수인 round()는 오사오입이다. 
# 즉, 5 초과일 때 올림한다는 것! 문제 조건에 맞추기 위해 round() 함수 안에 0.0000001를 더해주었다.
import sys
input = sys.stdin.readline
n = int(input())
if(n!=0):
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    arr.sort()
    x = round(n*0.15+0.0000001);
    s = sum(arr[x:n-x])
    ans = round((s/(n-2*x))+0.0000001)
    print(ans)
else:
    print(0)

    print(ans)

main()

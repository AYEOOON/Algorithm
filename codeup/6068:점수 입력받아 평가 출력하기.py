# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.


# 내 풀이 1

n = int(input())

if n>=90 :
  print('A')
else :
  if n>=70 :
    print('B')
  else :
    if n>=40 :
      print('C')
    else :
      print('D') 
      
      
# 내 풀이 2

n = int(input())

if n>=90 :
  print('A')
elif n>=70 :
    print('B')
elif n>=40 :
    print('C')
else :
    print('D') 

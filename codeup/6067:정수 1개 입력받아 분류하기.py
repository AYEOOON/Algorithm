# 0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.


n = int(input())

if n<0 :
  if n%2==0 :
    print('A')  
  else :
    print('B')
    
else :
  if n%2==0 :
    print('C')
  else :
    print('D')

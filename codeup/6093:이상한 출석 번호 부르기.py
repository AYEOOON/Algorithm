# 출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자.


n = int(input())
a = input().split()#입력 받을 때, 리스트를 받을 수 있다.

a=list(map(int,a))#얘는 map()을 이용해 리스트 a의 요소들을 모두 int()적용한 후, 그걸 리스트화 시키는 것이고.
'''
for i in range(n) : #얘는 반복문을 이용하여 각 요소에 직접 하나씩 접근하여 int()를 적용한 것.
  a[i] = int(a[i])
'''

for i in range(n-1,-1,-1):#뜻 잊지 말기
    print(a[i],end=' ')



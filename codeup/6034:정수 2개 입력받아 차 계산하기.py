# 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.


a,b=input().split()
c=int(a)-int(b)
print(c)


#다른 사람풀이

a,b = map(int,input().split())     # 변수 c를 사용하지 않고 바로 map이라는 파이썬 내장함수를 사용해서 변수 a,b를 정수로 입력받을수 있음
print(a-b)

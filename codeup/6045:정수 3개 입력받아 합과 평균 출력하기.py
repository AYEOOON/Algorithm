# 정수 3개를 입력받아 합과 평균을 출력해보자.


#내 풀이
a,b,c = map(int,input().split())
sum = a+b+c
avg = sum/3
print(sum, format(avg,".2f"))


#다른 사람 풀이
a,b,c = map(int,input().split())
print(a+b+c,"%.2f"%((a+b+c)/3))

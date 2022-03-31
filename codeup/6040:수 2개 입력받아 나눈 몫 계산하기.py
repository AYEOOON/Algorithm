# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.


#내 풀이
a,b = input().split()
a=int(a)
b=int(b)
print(a//b)



#다른 풀이
a, b = input().split()
print(int(a)//int(b))


# map을 사용한 다른 풀이

a,b = map(int,input().split())
print(a//b)

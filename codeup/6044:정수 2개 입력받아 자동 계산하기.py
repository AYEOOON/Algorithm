# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.

# 내 풀이
a,b=input().split()
c=int(a)+int(b)
d=int(a)-int(b)
e=int(a)*int(b)
f=int(a)//int(b)
g=int(a)%int(b)
h=int(a)/int(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print( format(h, ".2f") )


# 다른 풀이
a,b=input().split()
a=int(a)
b=int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(round(a/b,2))      # Round = 반올림할 숫자, 반올림할 자리수

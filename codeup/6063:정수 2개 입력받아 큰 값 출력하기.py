#입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자. 단, 3항 연산을 사용한다.


# 내 풀이
a,b = map(int,input().split())
if a > b:
    print(a)
else:
    print(b)
    
    
# 다른 풀이
a,b = map(int,input().split())
c = a if a>=b else b
print(c)

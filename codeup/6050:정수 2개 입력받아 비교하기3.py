# 두 정수(a, b)를 입력받아 b의 값이 a의 값 보다 크거나 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.


# 내 풀이
a,b = map(int,input().split())
if a<=b:
    print('True')
else:
    print('False')
    
    
# 다른 풀이 

a, b = map(int,input().split())
print(a<=b)


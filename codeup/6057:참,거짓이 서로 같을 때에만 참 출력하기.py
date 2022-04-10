# 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.


# 내 풀이
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
if ((c and d)) or ((not c and not d)):
    print('True')
else:
    print('False')

    
# 다른 풀이 1
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and b) or (not a and not b))


# 다른 풀이 2
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(a==b)


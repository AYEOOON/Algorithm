# 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.


# 내 풀이
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
if (not c) and (not d):
    print(True)
else:
    print(False)

    
# 다른 풀이 1
a, b = input().split()
c= bool(int(a))
d= bool(int(b))

print( not (c or d) )


#다른 풀이 2
a, b = input().split()
c= bool(int(a))
d= bool(int(b))

print( c==False and d==False )

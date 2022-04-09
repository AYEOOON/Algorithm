# 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.


# 내 풀이

a, b = map(int,input().split())
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))


# 다른 사람 풀이

a,b = map(int,input().split(' '))
if(bool(a) == True and bool(b) == False) :
    print(True)
elif(bool(a) == False and bool(b) == True) :
    print(True)
else :
    print(False)

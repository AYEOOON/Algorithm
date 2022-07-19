# 3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.


# 내 풀이
a, b, c = map(int,input().split())  # 주사위 3개의 수 입력

if a == b == c :     # 3개 모두 같을 때
    print(10000+a*1000)
elif a == b:
    print(1000+a*100)   # 2개 만 같을 때
elif a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:                  # 3개 다 다를 때
    M = max(a,b,c)     # 가장 큰 수
    print(M*100)

    
# 다른사람 풀이

lst = sorted(list(map(int, input().split())))

if len(set(lst)) is 1:
    print(10000 + lst[0]*1000)
elif len(set(lst)) is 2:
    print(1000 + lst[1]*100)  # pick middle
else:
    print(lst[2]*100)

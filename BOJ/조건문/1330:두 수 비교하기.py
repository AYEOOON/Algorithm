# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.


# 내 풀이

A, B = map(int,input().split())
if A > B:
    print('>')
elif A == B:
    print('==')
else:
    print('<')

    
# 다른사람 풀이

a, b = map(int, input().split())
print('>' if a > b else ('<' if a < b else '=='))

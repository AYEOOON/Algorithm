# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

# 내 풀이
def solution(n):
    for i in range(1, n+1):
        if i**2 == n:
            return (i+1)**2
            break
        
    return -1

# 내 풀이를 개선한 풀이
# n = 11이면 -1로 빠져야되는데 돌려보시면, sqrt(n)*sqrt(n)==n 이 성립되어 18.6332495807108 이란 값이 나온다.
# int()를 추가하고 해결함
def solution(n):
    return (n**.5+1)**2 if int((n**.5))**2 == n else -1


# 다른사람 풀이1
def nextSqure(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or -1


# 다른사람 풀이2
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1

# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# a와 b의 대소관계는 정해져있지 않습니다.

# 내 풀이
def solution(a, b):
    answer = 0
    if (a<b):
        for i in range(a, b+1):
            answer += i
        return answer
    else:
        for i in range(b, a+1):
            answer += i
        return answer

# 개선한 내 풀이
def solution(a, b):
    if (a<b):
        return sum(range(a,b+1))   # for문 없이 range만 쓸 수 있는지 몰랐다. 리스트를 출력함
    else:
        return sum(range(b,a+1))

# 다른사람 풀이1
def adder(a, b):
    if a > b:
        a, b = b, a   # a와 b 치환
    return sum(range(a, b + 1))


# 다른사람 풀이2(수열공식 이용) 
# abs() : 절댓값 함수
def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2  # n(n+1)/2


# 다른사람 풀이3(min, max 를 이용한 풀이)
def adder(a, b):
    return sum(range(min(a, b), max(a, b)+1))

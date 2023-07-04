# 짝수면 "Even"을 출력하고, 홀수면 "Odd"를 출력하는 함수 만드는 문제

# 내 풀이
# 삼항연산자를 써서 푼 풀이
def solution(num):
    return "Even" if num%2 == 0 else "Odd"

# 람다를 이용해 푼 풀이
solution = lambda num: "Even" if num%2==0 else "Odd"


# 다른사람 풀이
# 논리연산자를 사용한 풀이
# num%2가 0이 아닐 때만 True 이기 때문에 Odd가 되고 그 외에는 Even!! (num % 2 and 'Odd') or 'Even'
def evenOrOdd(num):
    if num%2:
        return "Odd"

    return "Even"

# 풀이를 삼항연산자로 고친것
def solution(num):
    return "Odd" if num%2 else "Even"

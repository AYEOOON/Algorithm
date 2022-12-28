# num1,num2가 매개변수로 입력될 때 몫을 answer로 리턴하는 문제

# 내 풀이

def solution(num1, num2):
    answer = num1//num2
    return answer


# 다른 사람 풀이

solution = int.__floordiv__

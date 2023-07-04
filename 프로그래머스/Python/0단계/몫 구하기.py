# 정수 num1, num2가 매개변수로 주어질 때, num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성하는 문제.

# 내 풀이

def solution(num1, num2):
    answer = num1//num2
    return answer


# 다른 사람 풀이

solution = int.__floordiv__

# 두 정수 left와 right가 매개변수로 주어집니다. 
# left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
# 약수의 갯수가 홀수인 경우는 제곱수인 경우밖에 없다는 것을 이용하여 풀었다. 

# 내 풀이
import math

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if (i**(0.5)).is_integer():
            answer -= i
        else:
            answer += i
    return answer


# 다른사람 풀이
def solution(left, right):
    return sum(n if (n ** 0.5) % 1 else -n for n in range(left, right + 1))

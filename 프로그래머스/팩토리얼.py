# 정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.
# 못푼문제


# 풀이

from math import factorial

def solution(n):
    k = 10
    while n< factorial(k):
        k -= 1
        
    return k

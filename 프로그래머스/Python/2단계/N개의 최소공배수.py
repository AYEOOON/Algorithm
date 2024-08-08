"""
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 
예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
"""

# a와 b의 최소공배수 = a*b // 최대 공약수

# 내 풀이
import math

def solution(arr):
    list = [arr[0]]
    
    for i in range(len(arr)):
        gcd = math.gcd(arr[i], list[-1])  # 제일 마지막에 있는 숫자 = 마지막으로 구한 최소공배수
        lcm = arr[i]*list[-1] // gcd
        
        list.append(lcm)
        
    return max(list)
  

# 다른사람 풀이
from fractions import gcd  # 아마 math 함수


def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer) // 최소 공배수를 바로 저장하는 식으로 풀었다!

    return answer

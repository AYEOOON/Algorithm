# 첫 번째 분수의 분자와 분모를 뜻하는 denum1, num1, 두 번째 분수의 분자와 분모를 뜻하는 denum2, num2가 매개변수로 주어집니다. 
# 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성하는 문제. 
# 풀지 못해 다른사람의 풀이를 참고하여 풀었다. 


# 풀이1

import math

def LCM(n1, n2): #최소공배수
    temp = math.gcd(n1, n2)
    return n1*n2/temp

def solution(denum1, num1, denum2, num2):
    top = denum1*num2 + denum2*num1
    bottom = num1*num2
    n = math.gcd(top, bottom)
    if n == 1:
        return [top, bottom]
    else:
        return [top/n, bottom/n]


# 풀이2

import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]

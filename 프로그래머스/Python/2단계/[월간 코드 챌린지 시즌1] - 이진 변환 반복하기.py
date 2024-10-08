"""
0과 1로 이루어진 어떤 문자열 x에 대한 이진 변환을 다음과 같이 정의합니다.

    1. x의 모든 0을 제거합니다.
    2. x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.

0과 1로 이루어진 문자열 s가 매개변수로 주어집니다. 
s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때, 
이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return 하도록 solution 함수를 완성해주세요.
"""

# 내 풀이
def solution(s):
    count_zero = 0
    cnt = 0
    
    while s != '1':
        count_zero += s.count('0')
        s = s.replace('0','')
        s = str(bin(len(s)))[2::]
        cnt += 1
        
    return [cnt, count_zero]


# 다른 사람 풀이
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]

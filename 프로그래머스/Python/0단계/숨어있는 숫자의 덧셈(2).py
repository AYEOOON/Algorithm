# 문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. 
# my_string안의 자연수들의 합을 return하도록 solution함수를 완성하는 문제
# 정규표현식을 사용함


# 내 풀이

import re

def solution(my_string):
    answer = re.findall(r'[0-9]+', my_string)
    result = 0
    for i in answer:
        result += int(i)
    return result


# 다른사람 풀이(정규표현식X)

def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())

  
# 다른사람 풀이(정규표현식O)

import re

def solution(my_string):
    return sum([int(i) for i in re.findall(r'[0-9]+', my_string)])

"""
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요
"""
"""
처음에 replace로 풀려고 했는데, 모두 치환된 후 생긴 또 다른 괄호쌍을 처리하지 못해 스택을 이용하여 풀었다.
"""

# 내 풀이
def solution(s):
    arr = []
    for i in s:
        if i == '(':
            arr.append('(')
        elif i == ')':
            if len(arr) == 0:
                return False
            else:
                arr.pop()
    return True if len(arr) == 0 else False

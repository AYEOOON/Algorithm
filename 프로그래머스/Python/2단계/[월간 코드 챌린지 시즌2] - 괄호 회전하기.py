"""
다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.

(), [], {} 는 모두 올바른 괄호 문자열입니다.
만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다. 
예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다. 
예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.

대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 
이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.
"""

# 괄호 문제는 조건식을 어떻게 해야할지가 중요한 것 같다.

# 내 풀이
def is_right(s):
    stack = []
    for i in s:
        if (len(stack) == 0):
            if (i == ']' or i == '}' or i == ')'):
                return False
            else: 
                stack.append(i)
        else:
            if i == ']':
                if stack[-1] == '[':
                    stack.pop()
                else: 
                    return False
            elif i == ')':
                if stack[-1] == '(':
                    stack.pop()
                else: 
                    return False
            elif i == '}':
                if stack[-1] == '{':
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(i)     
    if len(stack) == 0:
        return True
    else:
        return False

def solution(s):
    cnt = 0
    n = len(s)
    
    for i in range(n):
        
        if is_right(s):
            cnt += 1
            s += s[0]
            s = s[1::]
        else:
            s += s[0]
            s = s[1::]

    return cnt



# 다른사람 풀이
def is_valid(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        elif stack[-1] == '(':
            if ch==')': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '{':
            if ch=='}': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '[':
            if ch==']': stack.pop()
            else: stack.append(ch)

    return False if stack else True

def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += is_valid(s[i:]+s[:i])
    return answer

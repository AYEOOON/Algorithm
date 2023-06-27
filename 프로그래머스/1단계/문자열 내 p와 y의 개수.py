# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
# 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

# 내 풀이
def solution(s):
    s = s.upper()
    for i in s:
        if s.count("P") == s.count("Y"):
            return True
        elif s.count("P") != s.count("Y"):
            return False
        elif "P" not in s and "Y" not in s:
            return True
        
    

# 다른사람 풀이
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')  # True/False 판별

# 다른사람 풀이
from collections import Counter
def numPY(s):
    c = Counter(s.lower())
    return c['y'] == c['p'] # Counter 생성자는 여러 형태의 데이터를 인자로 받음. 먼저 중복된 데이터가 저장된 배열을 인자로 넘기면 각 원소가 몇 번씩 나오는지가 저장된 객체를 얻게 된다
    

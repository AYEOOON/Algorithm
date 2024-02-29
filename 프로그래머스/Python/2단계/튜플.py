"""
튜플은 다음과 같은 성질을 가지고 있습니다.

1. 중복된 원소가 있을 수 있습니다. ex : (2, 3, 1, 2)
2. 원소에 정해진 순서가 있으며, 원소의 순서가 다르면 서로 다른 튜플입니다. ex : (1, 2, 3) ≠ (1, 3, 2)
3. 튜플의 원소 개수는 유한합니다.

원소의 개수가 n개이고, 중복되는 원소가 없는 튜플 (a1, a2, a3, ..., an)이 주어질 때(단, a1, a2, ..., an은 자연수), 이는 다음과 같이 집합 기호 '{', '}'를 이용해 표현할 수 있습니다.
{{a1}, {a1, a2}, {a1, a2, a3}, {a1, a2, a3, a4}, ... {a1, a2, a3, a4, ..., an}}

특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때, s가 표현하는 튜플을 배열에 담아 return 하도록 solution 함수를 완성해주세요.
"""
"""
집합에서 "가장 빈번히 나온 숫자" 순으로 튜플이 구성된다.
{{1, 2, 3}, {2, 1}, {1, 2, 4, 3}, {2}} 이 집합을 보면 '2'가 4번나오니까 튜플의 가장 맨앞 숫자가 '2'라는 것을 유추할 수 있다.
"""

# 내 풀이
def solution(s):
    answer = []
    s = s.replace("{", '')
    s = s.replace("}", '')
    s = s.split(',')
    dic = dict.fromkeys(s, 0)
    for i in s:
        dic[i] += 1
    
    arr = sorted(dic.items(),reverse = True, key=lambda item: item[1])
    
    for j in arr:
        answer.append(int(j[0]))
    return answer


# 다른사람 풀이(정규표현식)
def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter


# 다른사람 풀이(나와 비슷한 풀이)
def solution(s):
    s = eval(s.replace("{", "[").replace("}", "]"))  # eval : 매개변수로 받은 expression (=식)을 문자열로 받아서, 실행하는 함수
    answer = list({num:0 for k in sorted(s, key=lambda x: len(x)) for num in k}.keys())
    return answer

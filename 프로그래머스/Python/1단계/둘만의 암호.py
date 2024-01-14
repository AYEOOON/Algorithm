""" 
두 문자열 s와 skip, 그리고 자연수 index가 주어질 때, 다음 규칙에 따라 문자열을 만들려 합니다. 암호의 규칙은 다음과 같습니다.

문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿔줍니다.
index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아갑니다.
skip에 있는 알파벳은 제외하고 건너뜁니다.

두 문자열 s와 skip, 그리고 자연수 index가 매개변수로 주어질 때 위 규칙대로 s를 변환한 결과를 return하도록 solution 함수를 완성해주세요
"""

# 내 풀이
def solution(s, skip, index):
    aph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    answer = ''
    for i in skip:
        if i in aph: # 이 줄은 없어도 될 것같다. 
            aph.pop(aph.index(i))
    for j in s:
        
        answer += aph[(aph.index(j)+index)%len(aph)]
    
    return answer



# 다른사람 풀이
from string import ascii_lowercase

def solution(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)  # 문자열을 더할수 있으면 뺄수도 있다! 
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]

    return result

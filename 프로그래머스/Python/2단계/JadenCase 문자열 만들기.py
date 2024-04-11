"""
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 
단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
"""
"""
공백 문자열이 나올 수 있다는 것을 주의해야한다
"""

# 내 풀이
def solution(s):
    answer = []
    word = s.split(" ")  # 공백을 구분하여 문자열 분리
    for i in word:
        if i != "": # 문자열이 공백이 아니면
            answer.append(i[0].upper() + i[1:].lower()) # 처음꺼 대문자, 그 뒤부터 소문자
        else:
            answer.append("") # 공백이면 ''추가

    return " ".join(answer) 구분자를 공백으로 문자열로 합치기


# 다른사람 풀이
def Jaden_Case(s):
    return s.title()  # 문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자로, 나머지는 소문자로 변환하는 함수

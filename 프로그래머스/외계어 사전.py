# 알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다.
# spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.


# 내 풀이

def solution(spell, dic):
    spell = set(spell) 
    for i in dic:
        if spell.issubset(set(i)):   # 부분집합인지 확인하는 함수
            return 1 
    return 2
  
  
# 다른사람 풀이

def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2

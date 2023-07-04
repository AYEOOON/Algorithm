# s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.
# count()를 사용하는 문제


# 내 풀이

def solution(s):
    answer = []
    for i in s:
        if s.count(i) == 1:
            answer.append(i)
            
    return ''.join(sorted(answer))
  
  
# 다른사람 풀이

def solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer

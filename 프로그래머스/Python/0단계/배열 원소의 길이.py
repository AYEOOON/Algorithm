# 문자열 배열 strlist가 매개변수로 주어집니다. 
# strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.


# 내 풀이

def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer

# 다른사람 풀이1

def solution(strlist):
    answer = list(map(len, strlist))
    return answer
    
    
# 다른사람 풀이2

def solution(strlist):
    return [len(str) for str in strlist]
    
    
# 다른사람 풀이3

def solution(strlist):
    return list(map(lambda v: len(v), strlist))

# 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성하는 문제.


# 내 풀이

def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i*2)
    return answer
  
  
# 다른사람 풀이1

def solution(numbers):
    return [num*2 for num in numbers]  # 리스트 컴프리헨션: [표현식 for 항목 in 반복가능객체 if 조건문] 
  
# 다른사람 풀이2

def solution(numbers):
    return list(map(lambda x: x * 2, numbers))

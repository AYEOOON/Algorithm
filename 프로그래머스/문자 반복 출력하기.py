# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

# 내 풀이

def solution(my_string, n):
    answer = []
    for i in my_string:
        answer.append(i*n)
        
    return ''.join(answer)    # ''.join(리스트)를 이용하여 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환
  
  
# 다른사람 풀이

def solution(my_string, n):
    return ''.join(i*n for i in my_string)

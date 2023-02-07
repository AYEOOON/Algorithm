# 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.


# 풀이1

def solution(my_string):
    answer = []
    for i in my_string:
        try:
            answer.append(int(i))
        except:
            continue
    return sum(answer)
  
  
# 풀이2

def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())

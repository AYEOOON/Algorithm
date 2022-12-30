# 정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성하는 문제.

# 내 풀이

def solution(n):
    answer = []
    for i in range (n+1):
        if i%2 ==1:
            answer.append(i)
    return answer
  
  
  
 # 다른사람 풀이

def solution(n):
    return [i for i in range(1, n+1, 2)]

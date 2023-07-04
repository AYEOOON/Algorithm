# 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.


# 내 풀이

def solution(num_list):
    even = 0 
    odd = 0
    for i in num_list:
        if i%2 == 0:
            even += 1
        elif i%2 == 1:
            odd += 1
    return [even, odd]
  
  
# 다른사람 풀이

def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer

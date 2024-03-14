"""
자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.
자연수 n이 매개변수로 주어질 때, 
연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.
"""

# 내 풀이
def solution(n):
    answer = 0
    num = 1
    
    while n>0:
        if n%num == 0:
            answer += 1
            n -= num
            num += 1
        else:
            n -= num
            num += 1
            
    return answer

# 다른사람 풀이
# 주어진 수보다 작은 홀수로 나누어 떨어지는 값의 갯수가 답이 됨
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])

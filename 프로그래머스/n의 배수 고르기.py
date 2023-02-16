# 정수 n과 정수 배열 numlist가 매개변수로 주어질 때, numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.


# 내 풀이

def solution(n, numlist):
    answer = []
    [answer.append(i) for i in numlist if i%n == 0]
    return answer
  
  
# 다른사람 풀이1( 내 풀이를 더 줄인 버전)

def solution(n, numlist):
    answer = [i for i in numlist if i%n==0]
    return answer
  
  
# 다른사람 풀이2( lambda 표현식을 활용한 버전)

def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))

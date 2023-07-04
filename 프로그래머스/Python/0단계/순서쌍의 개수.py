# 순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다.
# 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.
# 풀지 못한 문제

# 풀이1

def solution(n):
    answer = []
    for i in range(1,n+1):
        if n % i == 0:
            answer.extend([(i, n//i)])    # extend는 리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 넣음
    return len(answer) 
  
  
# 풀이2

def solution(n):
    return len(list(filter(lambda v: n % (v+1) == 0, range(n))))
  
# lambda v는 n을 v+1로 나눴을 때 나머지가 0이 되는 값을 range n까지 모두 산출된다. 
# 이 값을 리스트로 묶어 길이를 구하면 된다.
  
  
# 풀이3

def solution(n):
    return len([number for number in range(1, n+1) if n%number == 0])

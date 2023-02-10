# 자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
# 풀지 못함

# 풀이1

def solution(n):
    prime_factor = []    # 소인수를 저장할 list를 선언
    answer = []
    
    i = 2         # while문에서 사용할 i를 2로 선언한다.(1보다 큰 소인수를 위해 2부터 시작한다.)
    
    while i<=n:   # i가 n보다 작을 때 까지만 반복
        if n%i == 0:  # 2부터 시작해서 i로 나누어 떨어지면 리스트에 append()해준다. 
            prime_factor.append(i)
            n = n//i   # 나누어 떨어지면 n값을 n을 i로 나눈 몫으로 업데이트한다.
            
        else:
            i += 1
            
    print(prime_factor)
    
    for i in prime_factor:       # 중복된 요소를 제거한다.
        if i not in answer:
            answer.append(i)
    return answer
  
  
  
# 풀이2

def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer

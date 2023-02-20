# 어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요. 
# 처음엔 2마리, 1시간 후엔 4마리, 2시간 후엔 8마리, ..., 10시간 후엔 2048마리가 됩니다. 따라서 2048을 return합니다.


# 내 풀이

def solution(n, t):
    for i in range(t):
        n += n     #  n *= 2 이런 식으로 써도 됨
        
    return n
    

# 다른사람 풀이1
# https://heestory217.tistory.com/81

def solution(n, t):
    return n << t    # << : 비스단위시프트연산자
                     # 왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고, 오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0 또는 양의 정수인 경우)이나 1(음의 정수인 경우)이 개수만큼 추가된다.

# 다른사람 풀이2

def solution(n, t):
    return n*(2**t)
    

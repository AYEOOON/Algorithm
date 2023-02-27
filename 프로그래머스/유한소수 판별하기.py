# 분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다. 유한소수가 되기 위한 분수의 조건은 다음과 같습니다.
# 기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.
# 두 정수 a와 b가 매개변수로 주어질 때, a/b가 유한소수이면 1을, 무한소수라면 2를 return하도록 solution 함수를 완성해주세요.
# https://chan-lab.tistory.com/34

# 내 풀이

import math

def solution(a, b):
    gcd = math.gcd(a,b) # a,b의 최대공약수를 구함
    b = b/gcd           # 분모 b를 최대공약수로 나눔
    
    while b%2 == 0:     # 각각 2와 5로 나누어 떨어진다면, while문에 집입
        b//=2
    while b%5 == 0:
        b//=5
    return 1 if b==1 else 2  # 최종적으로 b가 1인지 아닌지를 return 
  
  
# 다른사람 풀이(유클리도 호제법)

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)
      
      
# 다른사람 풀이(소인수분해)

def factorization(x):
    d = 2
    output = []
    
    while d <= x:
        if x % d == 0:
            output.append(d)
            x /= d          # 나누어 떨어진 몫을 x로 대체
        else:
            d += 1
            
    return output

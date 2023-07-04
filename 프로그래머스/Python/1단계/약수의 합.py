# 주어진 수의 약수를 더한 값을 리턴하는 함수를 만드는 문제
# 내 풀이
def solution(n):
    answer = []
    for i in range(1, n+1):
        if n%i == 0:
            answer.append(i)
    return sum(answer)
  

# 다른 사람 풀이
def sumDivisor(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])


# 다른 사람 풀이
def sumDivisor(num):
    return sum([i for i in range(1,num+1) if num%i==0])

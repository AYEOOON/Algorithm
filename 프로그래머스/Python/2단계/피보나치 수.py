# 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.
# 재귀를 사용하여 푸는 문제인줄 알았는데, 간단하게 배열과 반복문으로 해결하였다. 

# 내 풀이
def solution(n):
    fibo = []
    for i in range(0,n+1):
        if i == 0:
            fibo.append(0)
        elif i == 1:
            fibo.append(1)
        elif i == 2:
            fibo.append(1)
        else:
            fibo.append(fibo[i-1] + fibo[i-2])
    return fibo[n]%1234567


# 다른사람 풀이
def solution(n):
    
    pre = 0 # 이전 피보나치 수를 저장하는 변수 
    current = 1 # 현재 피보나치 수를 저장하는 변수
    
    # 2부터 n까지 순회
    for i in range(2, n+1):
        
        # 현재 피보나치 수는 이전 두 피보나치 수의 합
        # 이전 피보나치 수는 갱신하기 전의 현재 피보나치 수
        current, pre = current + pre, current
    
    # n번째 피보나치 수를 1234567로 나눈 나머지를 반환
    return current % 1234567

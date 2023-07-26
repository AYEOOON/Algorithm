# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

# 내 풀이
def solution(n):
    sosu = 0
    for i in range(2, n+1):
        if isPrime(i) == True:
            sosu += 1
        else: continue
    return sosu

def isPrime(n):
    for i in range(2, int(n**0.5)+1):  # 예를 들면 8의 경우 2*4 = 4*2와 같은 식으로 대칭을 이루기 때문에 제곱근까지만 확인하면 됨
        if n%i == 0:
            return False
    return True


# 다른사람 풀이(에라토스테네스의 체)
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.


# 내 풀이

def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
n = int(input())
print(fib(n))




# for문을 이용한 풀이

n = int(input())

fib = [0, 1]
for i in range(2, n+1):
    num = fib[i-1] + fib[i-2]
    fib.append(num)
print(fib[n])

# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.


# 내 풀이

def solution(n):
    evens = []
    for i in range(n+1):
        if i%2 == 0:
            evens.append(i)
        else:
            continue
    return sum(evens)
  
  
# 다른사람 풀이

def solution(n):
    return sum([i for i in range(2, n + 1, 2)])

# 정수 배열 a, b의 내적을 return 하도록 solution 함수를 완성해주세요.

# 내 풀이
def solution(a, b):
    sum = 0
    for i in range(len(a)):
        sum += a[i] * b[i]
        
    return sum

# 다른사람 풀이1
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])   # zip():양 측에 있는 데이터를 하나씩 차례로 짝을 지어줌.

# 다른사람 풀이2
solution = lambda x, y: sum(a*b for a, b in zip(x, y))

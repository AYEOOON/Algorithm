# 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴하는 함수를 완성하는 문제

# 내풀이
def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)  

    return answer

# 내 풀이를 개선한 것 
def solution(x, n):
    return [x*i for i in range(1,n+1)]


# 다른사람 풀이
def solution(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]
print(number_generator(2, 5))

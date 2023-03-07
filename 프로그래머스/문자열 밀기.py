# 문자열 A와 B가 매개변수로 주어질 때, A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를 return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.
# 풀지 못한 문제


# 풀이1

def solution(A: str, B: str):
    result = 0

    while result != len(A):
        if A == B:
            return result
        A = A[-1] + A[:-1]
        result += 1

    return -1
  

# 풀이2 

solution=lambda a,b:(b*2).find(a)


# 풀이3

def solution(A, B):
    #if A == "":
    #    return 0

    AA = A+A
    answer = AA.find(B)

    if answer >0:
        answer = len(A) - answer

    return answer

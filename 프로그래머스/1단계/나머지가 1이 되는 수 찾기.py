# 자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성하는 문제. 
# 왜 answer = i return answer은 안되고, return i는 될까..
# solution함수가 return 키워드를 만나면 스택 프레임에서 빠져나옴
# 그래서 for 내부에서 특정 조건을 만족시킬 경우 해당 함수를 바로 종료시킨다고 생각하면 될 것 같다.

# 내 풀이
def solution(n):
    for i in range(1,n+1):
        if n%i ==1:
            return i

# 다른사람 풀이
def solution(n):
    answer = min([x for x in range(1, n+1) if n % x == 1])  # 1로 나눠지는 수를 모두 리스트에 넣고, 최소값을 구하는 방법
    return answer

# 다른사람 풀이
solution = lambda n: min(list(filter(lambda x:n%x==1,range(1,n+1))))  # 나머지가 1인 숫자만 필터링하여 리스트로 감싼 후 최소값을 꺼내는 방법

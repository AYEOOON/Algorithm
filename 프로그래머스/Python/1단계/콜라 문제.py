# 콜라를 받기 위해 마트에 주어야 하는 병 수 a, 빈 병 a개를 가져다 주면 마트가 주는 콜라 병 수 b, 상빈이가 가지고 있는 빈 병의 개수 n이 매개변수로 주어집니다. 
# 상빈이가 받을 수 있는 콜라의 병 수를 return 하도록 solution 함수를 작성해주세요.

# 내 풀이
def solution(a, b, n):
    answer = 0
    while(n>=a):
        answer += b*(n//a)
        n = b*(n//a)+ (n%a)

    return answer


# 다른 사람 풀이
# 한꺼번에 계산하지 않고 a개만 팔고 b개를 받는 과정은 결국 a-b 개씩 병을 소비하는 것으로 생각, 
# 첫번째 진행할 때는 a개만 소비되기 때문에, b만큼 못받음(-b), 그 조건을 먼저 계산 n-b 반복횟수는 n-b // (a-b) 여기에 받는 병수 b 곱한 것
solution = lambda a, b, n: max(n - b, 0) // (a - b) * b

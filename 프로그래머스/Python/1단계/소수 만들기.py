# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.


# 내 풀이
from itertools import combinations

def solution(nums):
    answer = 0
    for i in combinations(nums,3):
        arr_sum = sum(i)
        for j in range(2, int(arr_sum ** 0.5)+1):
            if arr_sum%j == 0:
                break
        else:    # else문을 for문과 같은 줄에 쓰게되면, for문의 반복이 끝나고나서 else문이 실행되게 됩니다(break로 빠져나가지 않는다면)
            answer += 1
    return answer


# 다른사람 풀이
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer

# 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.


# 내 풀이 (조합을 사용한 풀이)
from itertools import combinations

def solution(numbers):
    answer = []
    arr = list(combinations(numbers,2))
    for i in arr:
        answer.append(sum(i))
    return sorted(list(set(answer)))



# 다른사람 풀이(조합을 사용하지 않은 풀이)
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))

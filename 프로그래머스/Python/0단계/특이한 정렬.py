# 정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.
# 따라서 매개변수 x가 numlist 배열을 돌면서, 각 요소와의 차이를 절댓값 method인 abs로 구한다.
# 이때 절댓값이 같은 값에 대한 handling을 위해서 내림차순(절댓값은 같지만 양수값을 우선순위가 더 높게 처리)으로 구현하기 위해 -x 로 부여한다.

# 풀이
def solution(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))  # 어떠한 기준을 삼아 정렬을 하는 문제는 lambda로 해결
    return answer

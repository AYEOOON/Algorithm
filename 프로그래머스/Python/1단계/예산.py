# 부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때, 최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록 solution 함수를 완성해주세요.
# 접근방법은 맞았지만 풀지 못한 문제


# 풀이1
# 최대한 많은 부서를 지원해줘야한다는 뜻은 적은 예산을 가진 팀들을 먼저 지원해주면 된다와 같다고 생각해서 d를 오름차순으로 정렬한 뒤 budget에서 빼주는 식
# 그래서 budget이 음수가 되면 빠져나오면 끝
def solution(d, budget):
    cnt = 0
    for i in d:
        budget -= i
        if budget < 0:
            break
        cnt += 1
    return cnt


# 풀이2
# 전체 부서별 신청 금액보다 예산이 크면 가장 큰 금액을 지원한 부서부터 하나씩 값을 빼서 예산 내에서 모든 부서를 지원할 수 있을 떄 부서의 수를 리턴
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

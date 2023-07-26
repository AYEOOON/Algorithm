# 실패율은 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.
# 예) N = 5, stages = [2, 1, 2, 6, 2, 4, 3, 3], result = [3,4,2,1,5]


# 내 풀이
def solution(N, stages):
    answer = []
    p = len(stages)
    fail = {i:0 for i in range(1,N+1)}
    
    for i in range(1,N+1):
        if p != 0:
            fail[i] = float(stages.count(i))/float(p)
            p -= stages.count(i)
        else: fail[i] = 0
        
    return sorted(fail, key= lambda x : fail[x], reverse = True)

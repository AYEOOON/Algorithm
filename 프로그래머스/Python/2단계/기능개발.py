"""
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 
이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 
각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.
"""


# 내 풀이
import math

def solution(progresses, speeds):
    answer = []
    remain = []
    for i in range(len(progresses)):
        remain.append(math.ceil((100 - progresses[i])/speeds[i]))    
    cnt = 0
    now = 0
    for j in range(len(remain)):
        if remain[now] >= remain[j]:
            cnt += 1
        else:
            answer.append(cnt)
            now = j
            cnt = 1
    answer.append(cnt) # 마지막 작업까지 넣기
    return answer


# 다른사람 풀이
# zip을 사용해서 작업과 속도를 묶은 뒤, 남은 시간을 계산하여 푼 풀이
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s): # ceil을 쓰지 않기 위해 음수를 이용(음수에서 내림은 절댓값이 커짐)
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

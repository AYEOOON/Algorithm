"""
채용 설명회에는 멘토 n명이 있으며, 1~k번으로 분류되는 상담 유형이 있습니다.
각 멘토는 k개의 상담 유형 중 하나만 담당할 수 있습니다. 멘토는 자신이 담당하는 유형의 상담만 가능하며, 다른 유형의 상담은 불가능합니다.
멘토는 동시에 참가자 한 명과만 상담 가능하며, 상담 시간은 정확히 참가자가 요청한 시간만큼 걸립니다.

참가자가 상담 요청을 하면 아래와 같은 규칙대로 상담을 진행합니다.

1. 상담을 원하는 참가자가 상담 요청을 했을 때, 참가자의 상담 유형을 담당하는 멘토 중 상담 중이 아닌 멘토와 상담을 시작합니다.
2. 만약 참가자의 상담 유형을 담당하는 멘토가 모두 상담 중이라면, 자신의 차례가 올 때까지 기다립니다. 참가자가 기다린 시간은 참가자가 상담 요청했을 때부터 멘토와 상담을 시작할 때까지의 시간입니다.
3. 모든 멘토는 상담이 끝났을 때 자신의 상담 유형의 상담을 받기 위해 기다리고 있는 참가자가 있으면 즉시 상담을 시작합니다. 이때, 먼저 상담 요청한 참가자가 우선됩니다.

참가자의 상담 요청 정보가 주어질 때, 참가자가 상담을 요청했을 때부터 상담을 시작하기까지 기다린 시간의 합이 최소가 되도록 각 상담 유형별로 멘토 인원을 정하려 합니다. 단, 각 유형별로 멘토 인원이 적어도 한 명 이상이어야 합니다.
상담 유형의 수를 나타내는 정수 k, 멘토의 수를 나타내는 정수 n과 참가자의 상담 요청을 담은 2차원 정수 배열 reqs가 매개변수로 주어집니다. 
멘토 인원을 적절히 배정했을 때 참가자들이 상담을 받기까지 기다린 시간을 모두 합한 값의 최솟값을 return 하도록 solution 함수를 완성해 주세요.
"""
"""
풀이
1. n명의 상담원에 대해 k개의 상담 유형이 매치되어있어야한다.(n>=k)
2. 참가자의 데이터를 유형별로 가공
3. 대기시간 구하기(각 유형은 독립적이다.)
4. 유형에 대한 대기시간 구하기
"""

# 내 풀이(다른사람 풀이 참고)
from itertools import combinations_with_replacement

def solution(k, n, reqs):
    answer = 999999999  # 최소의 시간을 구해야 하므로 큰 수 저장
    start_end = {i:[] for i in range(1,k+1)}  # 유형별로 참가자들의 시작, 끝 시간을 넣을 딕셔너리
    comb = list(combinations_with_replacement([i for i in range(k)],r=n-k))  # 중복조합을 사용하여 n-k개의 선택에 대한 조합을 구함
    
    cases = []
    for case in comb:
        base = [1 for _ in range(k)]  # 최소 1명의 멘토를 저장하고 
        for c in case:
            base[c]+=1  # 각 경우에 맞는 자리에 한명씩 더한 뒤 
            
        cases.append(base) # 모든 경우의 수에 추가
    
    for s, e, t in reqs: 
        start_end[t].append([s,s+e]) # 시작, 끝시간 저장
    
    for case in cases:
        wait = 0  # 각 유형은 독립적이므로, 각 유형에 대한 대기시간의 합이 각각의 경우의 대기시간이다. 
        for i in range(k):
            p = sorted(start_end[i+1], key = lambda x:x[0]) # 시작시간을 기준으로 정렬
            mento_list = [0 for _ in range(case[i])] # 각 멘토의 상담 종료 시간을 저장하는 배열
            for s, e in p:  # s = 시작시간, e = 끝시간
                mento_list = sorted(mento_list) # 종료시간이 가장 이른 곳에 배치하기 위해
                if mento_list[0] <= s:  # 만약 종료시간이 다음 시작시간보다 작다면
                    mento_list[0] = e  # 그 다음 상담종료시간 저장
                else: 
                    temp = mento_list[0] - s  # 대기시간
                    mento_list[0] = e + temp  # 상담 종료시간 + 기다려야하는 시간
                    wait += temp  # 대기시간 추가
            if wait > answer:
                break
        if wait < answer:
            answer = wait
        
    return answer
    

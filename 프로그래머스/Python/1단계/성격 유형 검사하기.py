# 나만의 카카오 성격 유형 검사지를 만들려고 합니다.
# 성격 유형 검사는 다음과 같은 4개 지표로 성격 유형을 구분합니다. 성격은 각 지표에서 두 유형 중 하나로 결정됩니다.
# 1번 지표	라이언형(R), 튜브형(T)
# 2번 지표	콘형(C), 프로도형(F)
# 3번 지표	제이지형(J), 무지형(M)
# 4번 지표	어피치형(A), 네오형(N)
# 매우 비동의(3), 비동의(2), 약간 비동의(1), 모르겠음(0), 약간 동의(1), 동의(2), 매우 동의(3)
# 각 질문은 1가지 지표로 성격 유형 점수를 판단합니다.
# 검사 결과는 모든 질문의 성격 유형 점수를 더하여 각 지표에서 더 높은 점수를 받은 성격 유형이 검사자의 성격 유형이라고 판단합니다.
# 단, 하나의 지표에서 각 성격 유형 점수가 같으면, 두 성격 유형 중 사전 순으로 빠른 성격 유형을 검사자의 성격 유형이라고 판단합니다.
# 질문마다 판단하는 지표를 담은 1차원 문자열 배열 survey와 검사자가 각 질문마다 선택한 선택지를 담은 1차원 정수 배열 choices가 매개변수로 주어집니다.
# 이때, 검사자의 성격 유형 검사 결과를 지표 번호 순서대로 return 하도록 solution 함수를 완성해주세요.


# 내 풀이
def solution(survey, choices):
    score = {"1": 3, "2": 2, "3": 1, "4": 0, "5": 1, "6": 2, "7":3}
    p = {"R": 0,"T": 0,"C": 0,"F": 0,"J": 0,"M": 0,"A": 0,"N": 0}
    arr = []
    yes = []
    no = []
    for i in survey:
        arr.append(list(i))
    for j in arr:
        yes.append(j[1])
        no.append(j[0])
        
    for k in range(len(choices)):
        if choices[k] > 4:
            p[yes[k]] += score[str(choices[k])]
        else:
            p[no[k]] += score[str(choices[k])]
            
    mbti = ''
    first = ['R','C','J','A']
    second = ['T','F','M','N']
    
    for f, s in zip(first, second):
        if p[f] < p[s]:
            mbti += s
        else:
            mbti += f
        
    return mbti



# 다른사람 풀이
def solution(survey, choices):
    answer = ''
    dic= {"R": 0,"T": 0,"C": 0,"F": 0,"J": 0,"M": 0,"A": 0,"N": 0 }
    
    for s,c in zip(survey,choices):
        if c>4:     dic[s[1]] += c-4
        elif c<4:   dic[s[0]] += 4-c
    
    li = list(dic.items())
    
    for i in range(0,8,2):
        if li[i][1] < li[i+1][1]: answer += li[i+1][0]
        else:   answer += li[i][0]
        
    return answer

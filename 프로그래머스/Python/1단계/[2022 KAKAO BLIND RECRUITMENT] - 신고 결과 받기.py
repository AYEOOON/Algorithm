"""
신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.

각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.

이용자의 ID가 담긴 문자열 배열 id_list, 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report, 정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때, 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.
"""

# 내 풀이
def solution(id_list, report, k):
    report = list(set(report))  # 동일한 유저에 대한 신고는 1회로 처리하기 위해 중복제거
    singo = {i:0 for i in id_list}  # 신고받은 유저의 신고 횟수
    mail = {i:0 for i in id_list}   # 신고한 유저의 정지된 유저 횟수
    jung_G = []  # 정지된 유저
  
    for i in report:
        a = i.split()  # a[0] : 신고한 유저, a[1] : 신고당한 유저
        singo[a[1]] += 1
    for n,s in singo.items():  # 신고된 유저의 신고횟수 세림
        if s >= k:  # 정해진 횟수보다 크면
            jung_G.append(n)  # 정지리스트에 추가
    for j in report:  
        b = j.split()
        if b[1] in jung_G:  # 정지리스트에 신고한 유저가 있으면
            mail[b[0]] += 1  # 횟수증가
            
    return list(mail.values())


# 다른사람 풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

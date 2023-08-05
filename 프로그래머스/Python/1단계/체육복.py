# 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.
# 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.
# 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 
# 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.
# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
# 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

# 처음 딕셔너리로 풀려다가 실패

# 내 풀이
def solution(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    
    for i in reserve[:]:  #   # 여벌있으면서 도난 당한 경우 
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    # 여벌이 있는 경우 빌려주고 lost 배열에서 제거   
    for j in reserve[:]:  # i-1, i+1번 학생이 모두 체육복을 도난 당한 경우, 여벌이 있는 i번째 학생은 i-1번 학생에게 체육복을 빌려준다. 
        if j-1 in lost:
            lost.remove(j-1)
        elif j+1 in lost:
            lost.remove(j+1)
            
    return n-len(lost)


# 다른사람 풀이
def solution(n, lost, reserve):
    
    a= set(lost)-set(reserve)    
    b= set(reserve)-set(lost)   #lost와 reserve 중복제거
    for i in b:     #체육복을 빌려줄 수 있을 때
        if i-1 in a:    #그 전 번호부터 확인해 봐야한다. 빌려줄 수 있을 때.
            a.remove(i-1)
        elif i+1 in a:  #그 다음 번호한테 빌려줄 수 있을 때
            a.remove(i+1)
            
                
    return n-len(a)

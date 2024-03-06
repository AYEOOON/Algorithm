"""
유사한 기사를 묶는 기준을 정하기 위해서 논문과 자료를 조사하던 튜브는 "자카드 유사도"라는 방법을 찾아냈다.

자카드 유사도는 집합 간의 유사도를 검사하는 여러 방법 중의 하나로 알려져 있다.
두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다.

자카드 유사도는 원소의 중복을 허용하는 다중집합에 대해서 확장할 수 있다. 
입력으로 들어온 두 문자열의 자카드 유사도를 출력한다. 
유사도 값은 0에서 1 사이의 실수이므로, 이를 다루기 쉽도록 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력한다.
"""
"""
set의 &, |를 이용하여 풀려고 하였으나 다중집합의 허용으로 인해 시간이 걸렸다.
"""

# 내 풀이
def solution(str1, str2):
    arr1 = []
    arr2 = []

    # str1을 두개씩 묶어 저장하는 부분
    start1 = 0
    end1 = 2
    for i in range(len(str1)-1):
        if str1[start1:end1].isalpha():
            arr1.append(str1[start1:end1].lower())
            start1 += 1
            end1 += 1
        else:
            start1 += 1
            end1 += 1

    # str2을 두개씩 묶어 저장하는 부분
    start2 = 0
    end2 = 2
    for j in range(len(str2)-1):
        if str2[start2:end2].isalpha():
            arr2.append(str2[start2:end2].lower())
            start2 += 1
            end2 += 1
        else:
            start2 += 1
            end2 += 1
    
    A = [] # 교집합
    B = [] # 합집합
    
    arr1_c = arr1.copy()
    B = arr1.copy()
    
    for k in arr2:
        # arr2의 요소 하나씩 가져오면서 만약 arr1_c안에 없으면 B에 k를 집어넣는다.
        # 만약 있다면 추가하지않고, arr1_c에서 k를 삭제하여 다중집합을 가능하게한다. 
        B.append(k) if k not in arr1_c else arr1_c.remove(k)
        
    for l in arr2:
        if l in arr1:
            arr1.remove(l)
            A.append(l)
        
    if len(A) > 0 and len(B) > 0:
        answer = len(A) / len(B) * 65536
    elif len(A) == 0 and len(B) == 0:  # A와 B모두 비어있으면 1에서 65536을 곱한것을 출력
        answer = 65536
    else:  # 하나면 비어있을 경우 0을 출력한다. 
        answer = 0
        
    return int(answer)


# 다른사람 풀이
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)

"""
어느 날 철호는 어떤 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 수가 모두 몇 가지인지 알아보고 싶어졌습니다. 
원형 수열이란 일반적인 수열에서 처음과 끝이 연결된 형태의 수열을 말합니다.
원형 수열은 처음과 끝이 연결되어 끊기는 부분이 없기 때문에 연속하는 부분 수열도 일반적인 수열보다 많아집니다.
원형 수열의 모든 원소 elements가 순서대로 주어질 때, 원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수를 return 하도록 solution 함수를 완성해주세요.
"""


# 내 풀이 (배열을 모두 순회하기 때문에 속도가 느림)
def solution(elements):
    hap = []
    
    n = len(elements)+1  # 원소의 갯수를 미리 저장해야함
    
    elements += elements[:-1]
    
    for i in range(n):
        for j in range(n):
            hap.append(sum(elements[i:j%n+i]))
            
    return len(list(set(hap))[1::])


# 다른사람 풀이(길이 별로 잘라서 모으는 것이 아닌, 하나를 잡고 거기서 부터 모든 길이를 다 자름)
def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)

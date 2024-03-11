"""
양의 정수 n이 주어집니다. 이 숫자를 k진수로 바꿨을 때, 변환된 수 안에 아래 조건에 맞는 소수(Prime number)가 몇 개인지 알아보려 합니다.

1. 0P0처럼 소수 양쪽에 0이 있는 경우
2. P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
3. 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
4. P처럼 소수 양쪽에 아무것도 없는 경우
    - 단, P는 각 자릿수에 0을 포함하지 않는 소수입니다.
    - 예를 들어, 101은 P가 될 수 없습니다

정수 n과 k가 매개변수로 주어집니다. 
n을 k진수로 바꿨을 때, 변환된 수 안에서 찾을 수 있는 위 조건에 맞는 소수의 개수를 return 하도록 solution 함수를 완성해 주세요.
"""
"""
split()을 이용하여 푸는 것이 핵심
진수 변환하는 부분을 외워두면 좋을 것같다. 
"""

# 내 풀이
def sosu(num):  # 소수 분별 함수
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    return True

def solution(n, k):
    result = []
    rev_base = ''

    # 진수 구하는 부분
    while (n > 0):
        n, mod = divmod(n, k)
        rev_base += str(mod)
    
    jinsu = rev_base[::-1]
    
    jinsu_split = jinsu.split('0') # 0을 기준으로 숫자 분리
    
    for i in jinsu_split:
        if len(i) == 0 or i == '1':
            continue
        if sosu(int(i)):
            #if ('0' + i + '0' in jinsu) or (i + '0' in jinsu) or ('0' + i in jinsu): # 굳이 없어도 되는 부분 
                #if '0' not in i:
                    result.append(i)
    
    
    return len(result)

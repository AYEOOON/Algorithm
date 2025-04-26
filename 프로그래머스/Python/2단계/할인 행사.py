"""
XYZ 마트는 일정한 금액을 지불하면 10일 동안 회원 자격을 부여합니다. 
XYZ 마트에서는 회원을 대상으로 매일 한 가지 제품을 할인하는 행사를 합니다. 
할인하는 제품은 하루에 하나씩만 구매할 수 있습니다. 
알뜰한 정현이는 자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰서 회원가입을 하려 합니다.

정현이가 원하는 제품을 나타내는 문자열 배열 want와 정현이가 원하는 제품의 수량을 나타내는 정수 배열 number, 
XYZ 마트에서 할인하는 제품을 나타내는 문자열 배열 discount가 주어졌을 때, 
회원등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수를 return 하는 solution 함수를 완성하시오. 
가능한 날이 없으면 0을 return 합니다.
"""

# 내 풀이
def solution(want, number, discount):
    memo = dict(zip(want, number))
    result = 0
    start = 0
    
    while(start <= len(discount)-10):
        good = 0
        for p in want:
            if memo[p] == discount[start:start+10].count(p):
                good +=1
                
        if good == len(want):
            result += 1
            start += 1
        else:
            start += 1
    
    return result


# 다른사람 풀이
from collections import Counter  # 딕셔너리처럼 사용가능
def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]): 
            answer += 1

    return answer

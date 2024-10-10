"""
레스토랑을 운영하던 스카피는 코로나19로 인한 불경기를 극복하고자 메뉴를 새로 구성하려고 고민하고 있습니다.
기존에는 단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성해서 새로운 메뉴를 제공하기로 결정했습니다. 
어떤 단품메뉴들을 조합해서 코스요리 메뉴로 구성하면 좋을 지 고민하던 "스카피"는 이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성하기로 했습니다.
단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다. 
또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함하기로 했습니다.

각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders, "스카피"가 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course가 매개변수로 주어질 때, 
"스카피"가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.
"""

# 내 풀이
from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    result = []
    
    # 각 코스 길이에 대해 처리
    for c in course:
        menu_count = defaultdict(int)  # 조합의 등장 횟수를 저장할 딕셔너리
        max_count = 0  # 가장 많이 주문된 횟수

        # 모든 주문을 순회
        for order in orders:
            # 각 주문에서 c개 조합 생성
            for comb in combinations(sorted(order), c):
                comb_str = ''.join(comb)  # 조합을 문자열로 변환
                menu_count[comb_str] += 1  # 카운트 증가
                max_count = max(max_count, menu_count[comb_str])  # 최대 등장 횟수 업데이트

        # 최대 등장 횟수에 해당하는 조합 필터링
        for key, value in menu_count.items():
            if value == max_count and value >= 2:  # 2명 이상 주문된 경우
                result.append(key)

    return sorted(result)  # 결과를 알파벳 순으로 정렬하여 반환


# 다른사람 풀이
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]


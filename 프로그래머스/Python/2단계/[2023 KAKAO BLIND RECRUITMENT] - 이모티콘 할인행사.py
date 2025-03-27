"""
1. 모든 할인율 조합 생성
- product(sale_rates, repeat=len(emoticons))을 이용해 이모티콘 개수만큼 할인율 조합을 만듦

2. 각 조합별 가입자 수 및 총 매출 계산
- users 리스트를 순회하며 각 사용자의 할인 기준과 최소 구매 금액을 확인
- 사용자가 원하는 할인율 이상이면 이모티콘을 구매하도록 계산

3. 이모티콘 플러스 가입 여부 판단
- 만약 사용자 제한가격이 총 가격보다 작으면 이모티콘 플러스 가입.
- 그렇지 않으면 구매 금액만 합산.

4. 최적의 경우 갱신
- max_join이 가장 많은 경우를 찾고, 같다면 max_price가 높은 경우를 선택
"""

from itertools import product  # 가능한 할인율 조합을 생성하기 위해 product 사용

def solution(users, emoticons):
    sale = [10, 20, 30, 40]  # 이모티콘에 적용할 수 있는 할인율 목록
    max_join = 0  # 최대 이모티콘 플러스 가입자 수
    max_price = 0  # 최대 매출액
    
    # 모든 이모티콘에 대해 가능한 할인율 조합을 생성
    sales_comb = list(product(sale, repeat=len(emoticons)))

    # 각 할인율 조합에 대해 최적의 결과 계산
    for sales in sales_comb:
        total_join = 0  # 현재 할인 조합에서의 총 가입자 수
        total_price = 0  # 현재 할인 조합에서의 총 매출액
        
        # 각 사용자별로 구매 여부 확인
        for limit_sale, limit_price in users:
            total_user = 0  # 해당 사용자의 총 구매 금액
            
            # 사용자가 구매하는 이모티콘 가격 계산
            for emoticon_price, s in zip(emoticons, sales):
                if limit_sale <= s:  # 사용자가 원하는 최소 할인율 이상이면 구매
                    total_user += emoticon_price * ((100 - s) / 100)  # 할인 적용된 가격 누적
            
            # 사용자의 총 구매 금액이 이모티콘 플러스 가입 기준을 넘으면 가입
            if total_user >= limit_price:
                total_join += 1
            else:
                total_price += total_user  # 가입하지 않으면 구매한 금액만 누적
        
        # 최대 가입자 수 및 매출 갱신
        # 1. 더 많은 가입자를 확보할 수 있는 경우 갱신
        # 2. 가입자 수가 동일하다면 매출이 높은 경우 갱신
        if max_join < total_join or (max_join == total_join and max_price < total_price):
            max_join, max_price = total_join, total_price
            
    return max_join, max_price  # 최적의 가입자 수와 매출 반환

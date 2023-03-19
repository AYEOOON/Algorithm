# 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급합니다. 
# 쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고, 서비스 치킨에도 쿠폰이 발급됩니다. 
# 시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때 받을 수 있는 최대 서비스 치킨의 수를 return하도록 solution 함수를 완성해주세요.
# 풀지 못한 문제


# 풀이

def solution(chicken):
    answer = 0
    coupon = chicken

    while coupon >= 10:
        eaten = coupon//10        # 쿠폰으로 먹은 치킨의 수
        answer += eaten           # 최대 서비스 치킨의 수
        coupon = coupon%10 + eaten   # 잔여 쿠폰의 수
    return answer 
  
  
  
# 풀이2

def solution(chicken):
    answer = (max(chicken,1)-1)//9
    return answer

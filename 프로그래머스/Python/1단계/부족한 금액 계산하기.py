# 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 
# 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
# 단, 금액이 부족하지 않으면 0을 return 하세요.

# 내 풀이
def solution(price, money, count):
    arr = []
    for i in range(1, count+1):  # 1부터 4까지 
        arr.append(price*i)  # 배열에 넣기
        
    if sum(arr) < money :  # 만약 돈이 부족하지 않을때
        answer = 0
    else:  # 돈이 부족할 때
        answer = sum(arr) - money
        
    return answer 

# 개선한 내 풀이
def solution(price, money, count):
    arr = [price*i for i in range(1, count+1)]
    return 0 if sum(arr) < money else  sum(arr) - money


# 다른사람 풀이 
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)

# 정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 soltuion 함수를 완성하는 문제.


# 내 풀이

solution = lambda num1,num2 : int(num1/num2*1000)  


# 다른사람 풀이

def solution(num1, num2):             # 지역변수 answer를 활용하지 않으면 좋은 점은 변수를 저장하기 위해선 비용이 들며, 비용이 늘면 시스템 성능의 저하가 올 수 있다.
    return int(num1 / num2 * 1000)    
  
# 또한 함수화 된 코드는 굳이 변수에 담지 않더라도 return 값으로 주면, 차후에 x = solution(someting) 같은 형태로 불러와서 사용이 가능함
# 따라서, 재사용이 없는 함수 내 지역변수는 굳이 변수에 담지 않는 것을 추천.

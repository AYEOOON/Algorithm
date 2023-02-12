#  머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때, 머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.


# 내 풀이

def solution(order):
    clap = 0
    for i in str(order):
        if i in ["3","6","9"]:
            clap += 1
            
    return clap
        
    
# 다른사람 풀이

def solution(order):
  return sum(map(lambda x: str(order).count(str(x)), [3,6,9]))

# 어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다
# signs배열이 boolean이라는 것에 초점을 맞춰야한다. 

# 내 풀이
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        elif signs[i] == False:
            answer -= absolutes[i]
            
    return answer

# 개선한 내 풀이
def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):  # zip(): 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer
  

# 다른사람 풀이1
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

# 위 풀이를 푼 것
def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer

# 다른사람 풀이2
def solution(absolutes, signs):
    answer = 0
    return sum([absolutes[i] *(1 if signs[i] else -1) for i in range(len(absolutes)

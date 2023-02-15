# 내 풀이

def solution(my_string):
    return eval(my_string)    # eval(): 매개변수로 받은 expression (=식)을 문자열로 받아서, 실행하는 함수
                              # eval("1+2") 라는 문자열이 매개변수로 들어오면 출력 값으로 3이라는 값을 반환
  
# 다른사람 풀이1

solution=eval


# 다른사람 풀이2

def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))  # -를 +-로 바꾸고 +로 split 해버려서 음수 만듦

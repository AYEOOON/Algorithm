#  "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요.
# ["Jane", "Kim"]	"김서방은 1에 있다"

# 내 풀이
def solution(seoul):
    answer = ("김서방은 %d에 있다" %seoul.index("Kim"))
    return answer

# 개선한 내 풀이 
# % 기호를 사용한 문자열 형식화를 이용하여 포매팅
def solution(seoul): 
    return ("김서방은 %d에 있다" %seoul.index("Kim"))


# 다른 사람 풀이
# format()을 이용하여 포매팅
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

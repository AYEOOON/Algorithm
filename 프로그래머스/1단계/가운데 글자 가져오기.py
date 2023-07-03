# 내 풀이
def solution(s):
    if len(s)%2:
        return s[len(s)//2] 
    else:
        return s[len(s)//2-1]+s[len(s)//2]
    return s


# 다른사람 풀이(슬라이싱을 이용한 풀이)
def solution(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]   # end: 슬라이싱을 끝낼 위치로 end는 포함하지 않는다!!


# 다른사람 풀이(람다를 이용한 풀이)
solution = lambda s: s[(len(s) - 1) // 2 : len(s) // 2 + 1]

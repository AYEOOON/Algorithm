# 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다.
# 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.


# 풀이1 

def solution(my_string):
    word = ("a,e,i,o,u")    # 영어 모음들을 저장해놓는다.
    for i in word:          # my_string의 문자열을 replace()를 이용하여 모음을 ""로 치환한다.
        my_string = my_string.replace(i,"")
    return my_string
  
  
# 풀이2

def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])

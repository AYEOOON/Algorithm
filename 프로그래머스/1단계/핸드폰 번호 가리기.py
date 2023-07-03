# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

# 내 풀이
def solution(phone_number):
    answer = ['*' for i in range(len(phone_number)-4)]
    return ''.join(answer) + phone_number[-4::]

# 조금 더 줄인 풀이
def solution(phone_number):
    return ''.join(['*' for i in range(len(phone_number)-4)]) + phone_number[-4::]
  

# 다른 사람풀이1
def hide_numbers(s):
    return "*"*(len(s)-4)+s[-4:] # 문자열도 곱셈이 가능하다.

# 다른 사람풀이2 (정규 표현식을 이용한 풀이)
import re

def hide_numbers(s):
    p = re.compile(r'\d(?=\d{4})')   #re.compile() 명령을 통해 정규표현식을 컴파일하여 변수에 저장한 후 사용할 수 있다.
    return p.sub("*", s, count = 0)

# 표현식1(?=표현식2): 표현식1 뒤의 문자열이 표현식2와 매치되면 표현식1 매치.
# \d	숫자 [0-9]와 같다.
# 정규표현식을 () 안에 넣으면 그 부분만 그룹화된다. groups 메서드를 통해 그룹들을 튜플 형태로 리턴 할 수 있다.

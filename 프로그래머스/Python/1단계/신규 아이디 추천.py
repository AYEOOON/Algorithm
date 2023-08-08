# 아이디 규칙에 맞지 않는 아이디를 입력했을 때, 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발하는 것입니다.
# 다음은 카카오 아이디의 규칙입니다.

# 아이디의 길이는 3자 이상 15자 이하여야 합니다.
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

# 신규 유저가 입력한 아이디를 나타내는 new_id가 매개변수로 주어질 때, "네오"가 설계한 7단계의 처리 과정을 거친 후의 추천 아이디를 return 하도록 solution 함수를 완성해 주세요.


# 내 풀이
def solution(new_id):
    answer = ''
    
    #1
    new_id = new_id.lower()
    
    #2
    for i in new_id:
        if (i.isalpha()) or (i.isdigit()) or (i == '-') or (i == '_') or (i == '.'):
            answer += i
    #3
    while(answer.find('..') != -1):
        answer = answer.replace('..', '.')
    
    #4
    if len(answer) != 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) != 0 and answer[-1] == '.':
        answer = answer[:-1]
        
    #5
    if len(answer) == 0:
        answer = 'a'
        
    #6-1
    if len(answer) >= 16:
        answer = answer[0:15]
        #6-2
        if answer[-1] == '.':
            i = 0
            while(answer[-1] == '.'):
                i += 1
                answer = answer[0:15-i]
           
    #7
    if len(answer) <= 2:
        while(len(answer)!=3):
            answer += answer[-1]
        
    return answer


# 내 풀이 개선할 점
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c

    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')



# 다른사람 풀이(정규식)
# []: or(대괄호 안의 모든 문자)
# [^]: not(대괄호 안의 문자 외의 모든 문자)
# ^[]: 대괄호 안의 문자로 시작하는 문자열
# []$: 대괄호 안의 문자로 끝나는 문자열
# +: 1개 이상의 문자
import re

def solution(new_id):
    st = new_id
    # 1단계
    st = st.lower()
    # 2단계
    st = re.sub('[^a-z0-9\-_.]', '', st)
    # 3단계
    st = re.sub('\.+', '.', st)
    # 4단계
    st = re.sub('^[.]|[.]$', '', st)
    # 5단계
    st = 'a' if len(st) == 0 else st[:15]
    # 6단계
    st = re.sub('^[.]|[.]$', '', st)
    # 7단계
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

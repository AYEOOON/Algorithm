# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 
# 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.


# 내 풀이
def solution(s):
    arr = s.split(" ")   # 공백을 기준으로 문자를 나눠준다.
    answer = ''
    for i in arr:
        for j in range(len(i)):
            if j%2==0:  # 짝수인경우
                answer += i[j].upper()
            else:       # 홀수인경우
                answer += i[j].lower()
        answer += ' '
    return answer[0:-1]


# 다른사람 풀이
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

"""
고객의 약관 동의를 얻어서 수집된 1~n번으로 분류되는 개인정보 n개가 있습니다.
약관 종류는 여러 가지 있으며 각 약관마다 개인정보 보관 유효기간이 정해져 있습니다.
유효기간이 지났다면 반드시 파기해야 합니다.
오늘 날짜를 의미하는 문자열 today, 약관의 유효기간을 담은 1차원 문자열 배열 terms와 수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacies가 매개변수로 주어집니다. 
이때 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

today는 "YYYY.MM.DD" 형태로 오늘 날짜를 나타냅니다.
terms의 원소는 "약관 종류 유효기간" 형태의 약관 종류와 유효기간을 공백 하나로 구분한 문자열입니다.
"""
"""
term을 딕셔너리로 저장한 후 더할 년도와 개월을 구한다.
월이 12이상일 경우 년을 1년 더하고, 월에서 12를 뺀다.
일이 0일 경우 월을 -1하고 일을 28로 지정해준다.
"""

# 내 풀이
def solution(today, terms, privacies):
    answer = []
    today = today.split('.')
    term_dict = {}
    
    for t in terms:
        a,b = t.split()
        term_dict[a] = int(b)
        
    for p in range(len(privacies)):
        date, tr = privacies[p].split()
        y,m,d = date.split('.')
        
        #if term_dict[tr] >= 24:
        p_y = (term_dict[tr]//12)
        p_m = (term_dict[tr]%12)
            
        if int(m) + p_m > 12:
            p_y += 1
            p_m -= 12
            
        if int(d) == 0:
            p_m = p_m - 1
            d = 28

        # 조건문 부분에서 문제가 있었다. 
        if int(y) + p_y < int(today[0]):
            answer.append(p+1)
            
        elif int(y) + p_y == int(today[0]):
            if int(m) + p_m < int(today[1]):
                answer.append(p+1)
        
            elif int(m) + p_m == int(today[1]):
                if int(d) <= int(today[2]):
                    answer.append(p+1)

    return answer


# 다른사람 풀이
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire

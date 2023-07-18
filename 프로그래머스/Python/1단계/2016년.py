# 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.

# 내 풀이(라이브러리O)
import datetime

def solution(a, b):
    day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    x = datetime.date(2016, a, b)
    return day[x.weekday()]


# 다른사람풀이(라이브러리X)
def getDayName(a,b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(sum(month[:a-1])+b-1)%7]

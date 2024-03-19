"""
소스 파일 저장소에 저장된 파일명은 100 글자 이내로, 영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")만으로 이루어져 있다. 파일명은 영문자로 시작하며, 숫자를 하나 이상 포함하고 있다.

파일명은 크게 HEAD, NUMBER, TAIL의 세 부분으로 구성된다.

- HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상이다.
- NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 앞쪽에 0이 올 수 있다. 0부터 99999 사이의 숫자로, 00000이나 0101 등도 가능하다.
- TAIL은 그 나머지 부분으로, 여기에는 숫자가 다시 나타날 수도 있으며, 아무 글자도 없을 수 있다.

무지를 도와 파일명 정렬 프로그램을 구현하라.
"""
"""
1. HEAD, NUMBER, TAIL 적절히 파싱
2. 우선 순위대로 파일명 정렬해서 출력
"""

# 내 풀이
def solution(files):
    arr = []
    
    for file in files:
        HEAD, NUM, TAIL = '', '', ''
        for i in range(len(file)):
            if file[i].isdigit():
                HEAD = file[:i]
                NUM = file[i:]
                
                for j in range(len(NUM)):
                    if NUM[j].isdigit() == False:
                        TAIL = NUM[j:]
                        NUM = NUM[:j]
                        break
                    
                arr.append([HEAD, NUM, TAIL])  # 들여쓰기 부분 중요
                break  # 중요 
                    

    arr = sorted(arr, key = lambda x : (x[0].lower(), int(x[1])))
    
    return [''.join(i) for i in arr]
                

# 다른사람 풀이
import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b

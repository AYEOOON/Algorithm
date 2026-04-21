'''
https://school.programmers.co.kr/learn/courses/30/lessons/17683
: 재생 시간만큼 실제로 들린 멜로디를 만든 뒤, 기억한 멜로디가 포함된 곡 중 재생 시간이 가장 긴 곡을 찾는 문제

이 문제는 것보기엔 문자열 문제이지만, 
실제로는 "시간 계산 + 문자열 치환 + 정렬"이 핵심이다. 

1. 재생 시간 게산
time = (끝 시각) - (시작 시각)
-> 분 단위로 정확하게 계산 되어야하며, 단순히 단순히 "1230 - 1200" 이런 식으로 하면 틀린다..

2. # 처리 
C# → c
D# → d
...
-> "ABC" vs "ABC#" 이런 경우 구분해야 한다. 문자열 비교에서 "C"가 "C#"에 포함되는 문제 방지하기 위함이다. 

3. 실제 재생된 멜로디 만들기
played = (melody * (time // len(melody))) + melody[:time % len(melody)]
-> 음악은 재생 시간만큼 반복되며, 길면 반복, 짧으면 잘리도록 슬라이스를 사용하였다. 

4. 정답 선택 기준
answer.append((idx, time, title))
-> 정렬 기준은 재생 시간이 길고, 먼저 나온 순으로 정렬해야함다. 
'''

from collections import defaultdict

def solution(m, musicinfos):
    
    def cal_time(start, end):
        sh, sm = map(int, start.split(':'))
        eh, em = map(int, end.split(':'))
        
        return (eh * 60 + em) - (sh * 60 + sm)
    
    def convert(melody):
        melody = melody.replace('C#', 'c')
        melody = melody.replace('D#', 'd')
        melody = melody.replace('F#', 'f')
        melody = melody.replace('G#', 'g')
        melody = melody.replace('A#', 'a')
            
        return melody

    music_dict = defaultdict(str)
    m = convert(m)
    answer = []
    
    for idx, musicinfo in enumerate(musicinfos):
        start, end, title, melody = musicinfo.split(',')
        
        time = cal_time(start, end)
        melody = convert(melody)
        played = (melody * (time//len(melody))) + melody[:time%len(melody)]
        
        if m in played: 
            answer.append((idx, time, title))

    if not answer:
        return "(None)"
    
    answer = sorted(answer, key = lambda x: x[1], reverse = True)
    
    return answer[0][2]

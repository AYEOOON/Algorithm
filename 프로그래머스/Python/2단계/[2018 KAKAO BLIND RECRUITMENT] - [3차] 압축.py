"""
알고리즘 중에서 성능이 좋고 구현이 간단한 LZW(Lempel–Ziv–Welch) 압축을 구현하기로 했다.
LZW 압축은 다음 과정을 거친다.

1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
5. 단계 2로 돌아간다.

주어진 문자열을 압축한 후의 사전 색인 번호를 배열로 출력하라.
"""
"""
인덱스를 이용하여 슬라이싱으로 풀려고 하였으나 실패
다른사람의 풀이를 참고하여 배열을 갱신하는 방향으로 풀었다.
"""

# 내 풀이
def solution(msg):
    answer = [0] # 빈 배열이면 오류가 발생한다. 
    alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    word = ''
    
    for m in msg:
        word += m
        if word not in alph:
            alph.append(word)
            
            word = m
            answer.append(alph.index(word)+1)
            
        else:
            answer[-1] = alph.index(word)+1
                 
    return answer


# 다른사람 풀이
def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
    answer = []

    while True:
        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = len(d)+1
                msg = msg[i-1:]
                break

    return answer

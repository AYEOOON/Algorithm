"""
1. 각 단어를 큐에 넣고, 큐에서 하나씩 꺼내어 가능한 변환 단어로 이동
  - 변환한 단어가 목표 단어라면 그때의 단계 수가 최소 변환 횟수
  - 각 단어에서 변환할 수 있는 단어는 한 문자만 다른 단어들로만 변환 가능

2. 단어 간 차이가 1인 경우:
  - 두 단어가 한 문자만 다른지 확인하는 함수가 필요
  - 예를 들어, hit과 hot은 한 문자만 다르므로 변환 가능

3. 단어 변환을 위한 큐 사용:
  - 큐에는 (현재 단어, 현재 변환 횟수)가 들어감
  - 목표 단어에 도달하면 변환 횟수를 리턴하고, 목표 단어에 도달할 때까지 변환 가능한 모든 단어를 큐에 넣는다.
"""

import queue 

def solution(begin, target, words):
    # 목표 단어가 words에 없다면, 변환 불가능하므로 0을 반환
    if(target not in words):
        return 0
    
    # 큐를 초기화하고 시작 단어와 0번 변환 횟수를 넣음
    Q = queue.Queue()
    Q.put([begin, 0])
    
    # 큐가 빌 때까지 반복
    while(not Q.empty()):
        cur, cnt = Q.get()  # 큐에서 현재 단어(cur)와 변환 횟수(cnt)를 꺼냄
        
        # 현재 단어가 목표 단어와 같으면 변환 횟수(cnt)를 반환
        if(cur == target):
            return cnt
        
        # words 리스트의 각 단어와 현재 단어(cur)를 비교
        for word in words:
            tmp = 0  # 단어가 몇 문자만 다른지 세는 변수
            
            # 현재 단어(cur)와 비교할 단어(word)의 각 문자 차이 확인
            for j in range(len(word)):
                if(cur[j] != word[j]):  # 문자가 다르면 tmp를 1 증가
                    tmp += 1
            
            # 현재 단어와 비교 단어가 한 문자만 다르면 큐에 넣기
            if (tmp == 1):
                Q.put([word, cnt + 1])  # 변환 횟수를 1 증가시켜 큐에 추가
    
    return 0  # 목표 단어로 변환할 수 없는 경우 0을 반환

'''
https://school.programmers.co.kr/learn/courses/30/lessons/17685
: 각 단어를 찾을 때, 다른 단어와 구분되기 위해 최소 몇 글자를 입력해야 하는지 계산하고, 모든 단어에 대해 필요한 입력 횟수의 합을 구하는 문제

처음에는 모든 단어의 접두어를 하나씩 비교하려고 하였지만, 이 방식은 시간복잡도가 매우 커져 비효율적임
핵심은 다음과 같다. 
  - 단어를 정렬하면, 가장 비슷한 단어는 항상 양 옆에 위치한다.
따라서 각 단어는 앞 단어와 뒤 단어만 비교하면 충분하다.

[LCP 알고리즘]
두 문자열의 공통 접두사 길이를 구하는 알고리즘
예:
  "go" vs "gone" → LCP = 2
  "war" vs "warrior" → LCP = 3

[풀이 과정]
1. 단어 리스트를 사전순으로 정렬한다.
2. 각 단어에 대해 다음을 계산한다. 
  - 이전 단어와의 공통 접두사 길이
  - 다음 단어와의 공통 접두사 길이
3. 두 값 중 더 큰 값을 기준으로 판단한다.

[중요]
기본 경우
  - 필요한 입력 길이 = max(이전 LCP, 다음 LCP) + 1
    👉 공통 접두사 이후 한 글자를 더 입력해야 구분 가능

예외: 접두어 관계
  - 어떤 단어가 다른 단어의 완전한 접두어인 경우:
   👉 단어 전체를 입력해야 함, 이 경우에는 중간에 구분이 불가능하기 때문에 끝까지 입력해야 함

* 이련 문제는 "전체 비교"가 아닌 "정렬 후 인접 단어 비교"로 해결한다.
'''

def solution(words):
    answer = 0
    words.sort()
    
    def lcp(a, b):
        length = 0
        for i in range(min(len(a), len(b))):
            if a[i] == b[i]:
                length += 1
            else:
                break
        return length
    
    for i in range(len(words)):
        prev_count = lcp(words[i], words[i-1]) if i > 0 else 0
        next_count = lcp(words[i], words[i+1]) if i < len(words)-1 else 0
        if prev_count == len(words[i]) or next_count == len(words[i]):
            answer += len(words[i])
        else:
            answer += max(prev_count, next_count)+1
    
    return answer

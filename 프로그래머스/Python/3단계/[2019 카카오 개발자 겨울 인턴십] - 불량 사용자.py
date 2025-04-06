"""
<풀이 방향>
1. banned_id의 *을 .으로 변환하여 정규표현식 패턴으로 변환
2. matches 리스트를 만들어 각 banned_id와 매칭되는 user_id 목록을 저장
3. itertools.permutations을 사용하여 banned_id 개수만큼의 user_id 순열을 생성
4. 각 banned_id에 대해 하나씩 매칭되는지 검사
5. 중복된 조합을 방지하기 위해 set에 저장
6. 최종적으로 가능한 조합의 개수를 반환

<문법 정리>
1. 정규 표현식 (re.sub & re.fullmatch)
re.sub("\*", ".", ban)
  - * 문자를 정규 표현식에서 사용 가능한 .(임의의 문자)로 변환
  - 예: "fr*d*" → "fr.d."

re.fullmatch(pattern, string)
  - pattern과 string이 완전히 일치하는지 검사
  - 예: "frodo"가 "fr.d." 패턴과 일치하면 True 반환

2. 순열 (itertools.permutations)
permutations(user_id, len(banned_id))
  - user_id에서 banned_id 길이만큼의 모든 가능한 순열 생성
  - 예: ["A", "B", "C"]에서 길이 2인 순열 → [("A", "B"), ("A", "C"), ("B", "A"), ...]

3. 모든 조건을 만족하는지 확인 (all 함수)
  - 모든 banned_id 패턴이 user_id 조합에서 매칭되는지 검사
  - all() → 모든 요소가 True이면 전체 결과를 True로 반환
"""

import re
from itertools import permutations

def solution(user_id, banned_id):
    answer = set()  # 중복 방지를 위해 set 사용
    
    # 불량 사용자 ID를 정규식 패턴으로 변환 ('*' → '.')
    banned_id = [re.sub("\*", ".", ban) for ban in banned_id]

    # 각 불량 사용자 패턴에 매칭되는 사용자 ID 리스트 생성
    matches = []
    for ban in banned_id:
        match = [user for user in user_id if re.fullmatch(ban, user) is not None]
        matches.append(match)

    # user_id에서 banned_id 개수만큼의 모든 순열 생성
    allUserList = list(permutations(user_id, len(banned_id)))
    
    # 각 순열이 banned_id 조건을 만족하는지 검사
    for user in allUserList:
        if all(user[i] in matches[i] for i in range(len(banned_id))):
            answer.add(tuple(sorted(user)))  # 순서 무관하게 저장하여 중복 제거
    
    # 가능한 경우의 수 반환
    return len(answer)

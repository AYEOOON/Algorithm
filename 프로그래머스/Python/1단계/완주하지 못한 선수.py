# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 
# 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다. 
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.


# 내 풀이
def solution(participant, completion):
    answer = ''
    person = {participant[i]: 0 for i in range(len(participant))}
    
    for name in participant:
        person[name] += 1
    for com in completion:
        person[com] -= 1
    
    return ''.join([k for k, v in person.items() if v == 1])
  

# 다른사람 풀이1(Counter를 사용한 solution)
import collections
def solution(participant, completion):
    # 1. participant의 Counter를 구한다
    # 2. completion의 Counter를 구한다
    # 3. 둘의 차를 구하면 정답만 남아있는 counter를 반환한다
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    # 4. counter의 key값을 반환한다
    return list(answer.keys())[0]


# 다른사람 풀이2(Sort/Loop을 사용한 solution)
def solution(participant, completion):
    answer = ''

    # 1. 두 list를 sorting한다
    participant.sort()
    completion.sort()

    # 2. completeion list의 len만큼 participant를 찾아서 없는 사람을 찾는다
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]

    # 3. 전부 다 돌아도 없을 경우에는 마지막 주자가 완주하지 못한 선수이다.
    return participant[len(participant)-1]


# 다른사람 풀이3(Hash를 사용한 solution)
def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    
    # 1. Hash : Participant의 dictionary 만들기
    # 2. Participant의 sum(hash) 구하기
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    
    # 3. completion의 sum(hash) 빼기
    for comp in completion:
        sumHash -= hash(comp)
    
    # 4. 남은 값이 완주하지 못한 선수의 hash 값이 된다.
    return hashDict[sumHash]

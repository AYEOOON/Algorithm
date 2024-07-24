""" 
무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 
구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.
구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 
모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.
"""

# 구명보트는 최대 2명이 탈 수 있기 때문에 몸무게를 정렬하여 투 포인터를 사용한다. 
# 가장 작은 몸무게를 가진 사람과 가장 큰 몸무게를 가진 사람의 합을 기준으로 limit보다 크다면 몸무게가 큰 사람은 구명보트를 혼자 태우고
# 이렇게 계속하다보면 비로소 가장 몸무게가 작은 사람과 몸무게가 큰 사람이 2명이서 구명보트에 태워 보낼 수 있게 된다.

# 내 풀이
def solution(people, limit):
    people.sort()  # 몸무게를 정렬
    heavy = len(people)-1  # 제일 무거운사람
    light = 0  # 제일 가벼운사람
    boat = 0
    
    while(light <= heavy):
        if people[light] + people[heavy] > limit:  # 제일 무거운 사람과 가벼운 사람을 더한 것이 제한을 넘긴다면
            heavy -= 1  # 무거운 사람만 내보냄
            boat += 1  # 보트 추가 
        else:  # 제한보다 작다면 가벼운 사람과 무거운사람을 함께 내보냄
            light += 1 
            heavy -= 1
            boat += 1
          
    return  boat


# 다른사람 풀이
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer  # 짝 지었을때만 2명씩 나가니까 전체 인원에서 짝지은 수만 빼주면 보트의 수가 됨

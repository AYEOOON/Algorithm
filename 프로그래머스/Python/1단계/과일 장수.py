# 사과의 최대 점수 k, 한 상자에 들어가는 사과의 수 m, 사과들의 점수 score가 주어졌을 때, 과일 장수가 얻을 수 있는 최대 이익을 return하는 solution 함수를 완성해주세요.
# (최저 사과 점수) x (한 상자에 담긴 사과 개수) x (상자의 개수)

# 내 풀이
def solution(k, m, score):
    score.sort(reverse = True)
    arr = []
    answer = 0
    for i in range(0,len(score),m):
        arr.append(score[i:i+m])
        if len(arr[-1]) != m:
            arr.pop()
    for i in arr:
        answer += min(i)*m
    
    return answer


# 다른사람 풀이1
def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m

# 다른사람 풀이2
solution = lambda _, m, s: sum(sorted(s)[-m::-m]) * m

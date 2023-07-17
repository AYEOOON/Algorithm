# 내 풀이
def solution(name, yearning, photo):
    answer = []
    for i in photo:
        result = 0
        for j in i:
            if j in name:
                result+=(yearning[name.index(j)])
        answer.append(result)
    return answer


# 다른사람 풀이1(나와 같은 풀이)
def solution(이름, 점수, 사진):
    return [sum(점수[이름.index(j)] for j in i if j in 이름) for i in 사진]


# 다른사람 풀이2(딕셔너리 사용)
def solution(name, yearning, photo):
    dictionary = dict(zip(name,yearning))
    scores = []
    for pt in photo:
        score = 0
        for p in pt:
            if p in dictionary:
                score += dictionary[p]
        scores.append(score)
    return scores

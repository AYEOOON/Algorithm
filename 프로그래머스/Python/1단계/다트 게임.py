# 1. 다트 게임은 총 3번의 기회로 구성된다.
# 2. 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
# 3. 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
# 4. 옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
# 5. 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
# 6. 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
# 7. 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
# 8. Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
# 9. 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
# 0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.
# "점수|보너스|[옵션]"으로 이루어진 문자열 3세트.로 입력된다. 
# 예를 들면, 1S2D*3T	37	11 * 2 + 22 * 2 + 33

# 내 풀이
def solution(dartResult):
    answer = []
    dartResult = dartResult.replace("10", "A")
    for i in range(len(dartResult)):
        if dartResult[i] == "S": 
            if dartResult[i-1] == "A":
                answer.append(10)
            else: 
                answer.append(int(dartResult[i-1]))
        if dartResult[i] == "D":  
            if dartResult[i-1] == "A":
                answer.append(10**2)
            else: 
                answer.append(int(dartResult[i-1])**2)
        if dartResult[i] == "T":
            if dartResult[i-1] == "A":
                answer.append(10**3)
            else: 
                answer.append(int(dartResult[i-1])**3)
        if dartResult[i] == "*":
            a = answer.pop()
            if len(answer):
                answer[-1] *= 2
            answer.append(2*a)
        if dartResult[i] == "#":
            answer[-1] *= -1
    return sum(answer)


# 다른사람 풀이1(정규표현식 사용)
import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')  # '?'가 Quantifier 중의 하나인데, 0이나 1을 나타내는 연산자, 아예 없거나 한 개만 있을 때만 돌려달라는 의미 
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer


# 다른사람 풀이2
def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)

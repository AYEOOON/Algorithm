# 두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). 
# X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. 
# X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.
# 예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다.
# 두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.


# 내 풀이
def solution(X, Y):
    a = [0]*10
    b = [0]*10
    answer = ''
    for i in X:
        a[int(i)] += 1
    for j in Y:
        b[int(j)] += 1
    for k in range(9,-1,-1):
        answer += (str(k)*min(a[k],b[k]))
    if len(answer) == 0:
        return "-1"
    elif answer[0] == '0':
        return "0"
    return answer


# 다른사람 풀이
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer

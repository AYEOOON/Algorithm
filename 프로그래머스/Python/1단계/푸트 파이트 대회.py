#수웅이가 준비한 음식의 양을 칼로리가 적은 순서대로 나타내는 정수 배열 food가 주어졌을 때, 대회를 위한 음식의 배치를 나타내는 문자열을 return 하는 solution 함수를 완성해주세요.
# 예를 들어, 3가지의 음식이 준비되어 있으며, 칼로리가 적은 순서대로 1번 음식을 3개, 2번 음식을 4개, 3번 음식을 6개 준비했으며, 물을 편의상 0번 음식이라고 칭한다면,
# 두 선수는 1번 음식 1개, 2번 음식 2개, 3번 음식 3개씩을 먹게 되므로 음식의 배치는 "1223330333221"이 됩니다. 따라서 1번 음식 1개는 대회에 사용하지 못합니다.


# 내 풀이
def solution(food):
    me = []
    for i in range(1, len(food)):
        if food[i] == 1:
            continue
        else:
            for j in range(food[i]//2):
                me.append(i)
    me.append(0)
    other = list(reversed(me[0:len(me)-1]))
    answer = me+other
    return ''.join(map(str,answer))

# 개선한 내 풀이
def solution(food):
    me = ''
    for i in range(1, len(food)):
        me += (str(i)*int(food[i]/2))
    return me+'0'+ me[::-1]


# 다른사람 풀이1
def solution(food):
    answer ="0"
    for i in range(len(food)-1, 0,-1):
        c = int(food[i]/2)
        while c>0:
            answer = str(i) + answer + str(i)
            c -= 1
    return answer


# 다른사람 풀이2
def solution(food):
    first = ''.join(str(foodNumber) * (quantity // 2) for foodNumber, quantity in enumerate(food))
    second = first[::-1]
    answer = first + '0' + second


    return answer

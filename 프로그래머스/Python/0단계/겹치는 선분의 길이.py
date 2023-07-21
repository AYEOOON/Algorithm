# 선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.

# 풀이1(교집합, 합집합 사용)
def solution(lines):
    answer = []
    
    line1 = set(i for i in range(lines[0][0],lines[0][1]))
    line2 = set(i for i in range(lines[1][0],lines[1][1]))
    line3 = set(i for i in range(lines[2][0],lines[2][1]))

    # 각각의 집합체(선분)들을 & 연산자로 교집합을 구한 뒤, 최종적으로 겹치는 선분들을 | 연산자로 합집합을 구해 총 length를 return
    return len(list(line1 & line2 | line1 & line3 | line2 & line3))



# 풀이2(-100부터 100까지 순회)
def solution(lines):
    table = [set([]) for _ in range(200)] # -100~100까지 각 선분들의 등장 count 초기화
    for index, line in enumerate(lines):
        x1, x2 = line
        for x in range(x1, x2):
            table[x + 100].add(index) # 선분에 음수가 들어있을 수도 있으므로 +100

    answer = 0
    for line in table:
        if len(line) > 1:
            answer += 1

    return answer
    
    

# 바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때, n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.
# 십자 뒤집기 횟수(n)가 입력된다. 십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.


d = list(list(map(int, input().split())) for _ in range(19))
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for j in range(19):
        if d[j][y] == 0:
            d[j][y] = 1
        else:
            d[j][y] = 0

        if d[x][j] == 0:
            d[x][j] = 1
        else:
            d[x][j] = 0

for i in range(19):
    print(*d[i])

    
    
# 다른 풀이
    
# 1. 초기 십자 바둑판 입력
baduk = []
for _ in range(19):
    matrix = list(map(int,input().split()))
    baduk.append(matrix)
    
# 2. n과 좌표 값을 입력받고 그에 따라 십자 형태에 맞춰 흑->백, 백->흑으로 변환
n = int(input())
for _ in range(n):  # n번입력
    x, y = map(int(input().split()) # x와 y 좌표 입력
    for i in range(19): # 변환
        baduk[i][y-1] = 1 if baduk[i][y-1] == 0 else 0   # 0->1, 1->0으로 변환
        baduk[x-1][i] = 1 if baduk[x-1][i] == 0 else 0   # 0->1, 1->0으로 변환
               
# 3. 변환된 값을 한 줄 단위로 출력
for b in baduk:
    print(*baduk)           

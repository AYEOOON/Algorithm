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

# 정수 n 이 주어지면 높이와 너비가 n 인 직각 이등변 삼각형을 출력하도록 코드를 작성해보세요.
# 별 찍는 원리를 까먹어서 당황한 문제

# 내 풀이

n = int(input())
for i in range(n):
    for j in range(i+1):
        print('*', end = '')
    print()


# 다른사람 풀이

print('\n'.join('*' * (i + 1) for i in range(int(input()))))

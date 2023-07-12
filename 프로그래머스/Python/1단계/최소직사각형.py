# 모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다. 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.
# 어떤 모서리는 가로가 될 수도 있고 세로도 될 수가 있다. 
# 한 모서리를 가로라고 지정하면 다른 모서리는 세로가 되어야 옳다.
# 두 개의 모서리를 비교하여 큰 값을 전부 가로 작은 값을 전부 세로로 두면
# 각 모서리의 길이의 최댓값이 답이 된다. 


# 내 풀이
def solution(sizes):
    a = []
    b = []
    for i in sizes:
        if i[0]>i[1]:
            a.append(i[0])
            b.append(i[1])
        else:
            a.append(i[1])
            b.append(i[0])
    return max(a)*max(b)


# 다른사람 풀이1
# 반 나눠서 큰거중에 가장 큰거 * 작은거중에 가장 큰거
# 보기엔 좋지만 for문이 두개 돌아가기 때문에 효율성 면에선 좋지않음
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes) 


# 다른사람 풀이2
# sum(sizes, []): 스택 오버 플로우 (ex- a = [[1, 2], [3, 4], [5, 6]] => [1, 2, 3, 4, 5, 6])
# 모두 괄호를 푼 뒤 배열에 넣어 작은것 중에서 큰것과 곱한 가장 큰수를 출력
solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)

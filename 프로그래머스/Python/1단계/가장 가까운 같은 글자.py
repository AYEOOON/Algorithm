# 문자열 s가 주어졌을 때, s의 각 위치마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자가 어디 있는지 알고 싶습니다.
# 예를 들어, s="banana"라고 할 때,  각 글자들을 왼쪽부터 오른쪽으로 읽어 나가면서 다음과 같이 진행할 수 있습니다.
# 결과물은 [-1, -1, -1, 2, 2, 2]가 됩니다.
# 문자열 s이 주어질 때, 위와 같이 정의된 연산을 수행하는 함수 solution을 완성해주세요.

# 내 풀이
def solution(s):
    answer = []
    arr = ''
    for i in range(len(s)):
        if s[i] not in arr:
            arr += s[i]
            answer.append(-1)
        elif s[i] in arr:
            arr += s[i]
            answer.append(i-arr[0:i].rindex(s[i]))  # 0부터 현재 단어의 인덱스 앞까지 뒤에서 부터 순회
    return answer


# 다른사람 풀이
def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer

# 키 하나에 여러 문자가 할당된 경우, 동일한 키를 연속해서 빠르게 누르면 할당된 순서대로 문자가 바뀝니다.
# 예를 들어, 1번 키에 "A", "B", "C" 순서대로 문자가 할당되어 있다면 1번 키를 한 번 누르면 "A", 두 번 누르면 "B", 세 번 누르면 "C"가 되는 식입니다.
# 이 휴대폰 자판을 이용해 특정 문자열을 작성할 때, 키를 최소 몇 번 눌러야 그 문자열을 작성할 수 있는지 알아보고자 합니다.
# 1번 키부터 차례대로 할당된 문자들이 순서대로 담긴 문자열배열 keymap과 입력하려는 문자열들이 담긴 문자열 배열 targets가 주어질 때, 각 문자열을 작성하기 위해 키를 최소 몇 번씩 눌러야 하는지 순서대로 배열에 담아 return 하는 solution 함수를 완성해 주세요.
# 단, 목표 문자열을 작성할 수 없을 때는 -1을 저장합니다.

# 딕셔너리를 이용해서 keymap의 값들의 순서를 저장

# 내 풀이
def solution(keymap, targets):
    result = []
    board = {}
    for i in keymap:
        for j in range(len(i)):
            if i[j] in board:  # 딕셔너리 안에 키값이 존재하면
                if board.get(i[j]) > i.index(i[j]): # 만약 키 값이 새로운 키값보다 크면
                    board[i[j]] = i.index(i[j])+1 # 새로운 키값으로 저장
            else:
                board[i[j]] = j+1
                
    for target in targets:
        click = 0
        for t in target:
            if t in board:
                click += board[t]
            else:
                click = -1
                break  # break문이 없으면 target의 첫 번째 원소에 대한 횟수를 -1로 잡고 다음 문자열에 대해서 계속 횟수를 더해서 -1이 아닌 다른값을 넣게 됩니다.
        result.append(click)
    return result


# 다른사람 풀이
def solution(keymap, targets):
    answer = []
    hs = {}
    for k in keymap:
        for i, ch in enumerate(k):
            hs[ch] = min(i + 1, hs[ch]) if ch in hs else i + 1 # 새로운 값과 원래 값중 최소값을 저장

    for i, t in enumerate(targets):
        ret = 0
        for ch in t:
            if ch not in hs:
                ret = - 1
                break
            ret += hs[ch]
        answer.append(ret)

    return answer

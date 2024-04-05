"""
1부터 n까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기를 하고 있습니다. 영어 끝말잇기는 다음과 같은 규칙으로 진행됩니다.

1. 1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
2. 마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
3. 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
4. 이전에 등장했던 단어는 사용할 수 없습니다.
5. 한 글자인 단어는 인정되지 않습니다.

람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때, 
가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 하도록 solution 함수를 완성해주세요.
"""

# 내 풀이
def solution(n, words):
    turn = 1
    note = [words[0]]
    answer = []
    
    for i in range(1,len(words)):  
        if i%n == 0:
            turn += 1
        if words[i][0] == words[i-1][-1] and words[i] not in note:
            note.append(words[i])
        else:
            answer.append(i%n+1)
            answer.append(turn)
            break   

    return answer if len(answer) != 0 else [0,0]


# 개선한 내 풀이
def solution(n, words):
    answer = []
    note = [words[0]]
    
    for i in range(1,len(words)):  
        if words[i][0] == words[i-1][-1] and words[i] not in note:
            note.append(words[i])
        else:
            answer.append(i%n+1)
            answer.append(i//n+1)
            break 

    return answer if len(answer) != 0 else [0,0]


# 다른사람 풀이
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]  # p까지의 단어 슬라이스에서 단어가 중복되는지 확인
    else:
        return [0,0]

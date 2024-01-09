"""
수확한 귤의 크기가 일정하지 않아 보기에 좋지 않다고 생각한 경화는 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하고 싶습니다.

예를 들어, 경화가 수확한 귤 8개의 크기가 [1, 3, 2, 5, 4, 5, 2, 3] 이라고 합시다. 경화가 귤 6개를 판매하고 싶다면, 크기가 1, 4인 귤을 제외한 여섯 개의 귤을 상자에 담으면, 귤의 크기의 종류가 2, 3, 5로 총 3가지가 되며 이때가 서로 다른 종류가 최소일 때입니다.

경화가 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어집니다. 경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 하도록 solution 함수를 작성해주세요.
"""

# 내 풀이
def solution(k, tangerine):
    cnt = dict.fromkeys(tangerine, 0)
    for i in tangerine:
        cnt[i] += 1
    value = sorted(list(cnt.values()),reverse = True)
    answer = 0
    total = 0
    for i in range(len(value)):
        total += value[i]
        answer += 1
        if k <= total:
            break
    return answer


# 다른사람 풀이
import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)  # for문대신 딕셔너리에서 값을 세려준다. 

    for v in sorted(cnt.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer

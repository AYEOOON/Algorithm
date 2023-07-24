# 코니는 다음과 같은 규칙으로 카드에 적힌 단어들을 사용해 원하는 순서의 단어 배열을 만들 수 있는지 알고 싶습니다.
# 원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용합니다.
# 한 번 사용한 카드는 다시 사용할 수 없습니다.
# 카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다.
# 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없습니다.
# 큐 사용하여 해결

# 내 풀이
ef solution(cards1, cards2, goal):
    for i in goal:
        if cards1 and i == cards1[0]: cards1.pop(0)
        elif cards2 and i == cards2[0]: cards2.pop(0)
        else: return "No"

    return "Yes"

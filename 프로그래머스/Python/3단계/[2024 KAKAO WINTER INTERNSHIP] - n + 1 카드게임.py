"""
당신은 1~n 사이의 수가 적힌 카드가 하나씩 있는 카드 뭉치와 동전 coin개를 이용한 게임을 하려고 합니다. 
카드 뭉치에서 카드를 뽑는 순서가 정해져 있으며, 게임은 다음과 같이 진행합니다.

1. 처음에 카드 뭉치에서 카드 n/3장을 뽑아 모두 가집니다. (n은 6의 배수입니다.) 
당신은 카드와 교환 가능한 동전 coin개를 가지고 있습니다.

2. 게임은 1라운드부터 시작되며, 각 라운드가 시작할 때 카드를 두 장 뽑습니다. 
카드 뭉치에 남은 카드가 없다면 게임을 종료합니다.
뽑은 카드는 카드 한 장당 동전 하나를 소모해 가지거나, 동전을 소모하지 않고 버릴 수 있습니다.

3. 카드에 적힌 수의 합이 n+1이 되도록 카드 두 장을 내고 다음 라운드로 진행할 수 있습니다. 
만약 카드 두 장을 낼 수 없다면 게임을 종료합니다.

처음에 가진 동전수를 나타내는 정수 coin과 카드를 뽑는 순서대로 카드에 적힌 수를 담은 1차원 정수 배열 cards가 매개변수로 주어질 때,
게임에서 도달 가능한 최대 라운드의 수를 return 하도록 solution 함수를 완성해 주세요
"""
"""
<문제 요약>
1. 항상 6의 배수 만큼의 카드가 주어지며, 카드를 뽑는 순서는 정해져있다.
2. 턴마다 처음에 카드 2장을 뽑고, n+1이 되는 카드 두장을 뽑는다. 그렇게 하지 못할 경우 게임을 종료한다.
3. 뽑을 카드가 없는 경우에도 게임을 종료한다. 
4. 뽑을 카드는 한장에 코인 하나로 가지고 올 수 있다. 
5. 도달 가능한 최대 라운드 수를 구해야한다.

<문제 아이디어>
1. 카드 뭉치에서 항상 2장을 뽑아 사용가능한 배열에 저장
2. 처음 가지고 있는 배열에서 뽑은 2장에 카드에 적힌 수의 합이 n+1이 되면 그 카드 두장을 낸다.
3. 카드 두장을 낼 수 없는 상황이 생기면
   3-1. 코인이 1이상인 경우 
        - 내가 가지고 있는 카드에서 1장을 선택하고, 나머지 한장은 사용가능한 카드에서 1장을 선택
        - n+1이 되면 코인 1 감소, 라운드 1 증가
   3-2. 코인이 2이상인 경우
        - 사용가능한 카드에서 2장을 선택
        - n+1이 되면 코인 2 감소, 라운드 1 증가
"""

# 내 풀이
def check(arr1, arr2, n):
    arr = set(arr2)
    for card in arr1:
        if n-card in arr:
            arr1.pop(arr1.index(card))
            arr2.pop(arr2.index(n-card))
            return True
    return False

def solution(coin, cards):
    round = 1
    n = len(cards)
    deck = cards[len(cards)//3:]
    firstcard = cards[:n//3]
    getcard = []
    
    while coin >= 0 and deck:
        getcard.append(deck.pop(0))
        getcard.append(deck.pop(0))
        
        if check(firstcard, firstcard, n+1):
            pass
        elif coin >= 1 and check(firstcard, getcard, n+1):
            coin -= 1
        elif coin >= 2 and check(getcard, getcard, n+1):
            coin -= 2
        else:
            break
            
        round += 1
        
    return round
